// Copyright 2019 The TensorFlow Authors. All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
// =============================================================================


class Webcam {
    constructor(webcamElement) {
        this.webcamElement = webcamElement;
    }

    capture() {
        return tf.tidy(() => {
            const webcamImage = tf.browser.fromPixels(this.webcamElement);
            const reversedImage = webcamImage.reverse(1);

            const croppedImage = this.cropImage(reversedImage);
            const batchedImage = croppedImage.expandDims(0);
            return batchedImage.toFloat().div(tf.scalar(127)).sub(tf.scalar(1));
        });
    }

    cropImage(img) {
        const size = Math.min(img.shape[0], img.shape[1]);
        const centerHeight = img.shape[0] / 2;
        const beginHeight = centerHeight - (size / 2);
        const centerWidth = img.shape[1] / 2;
        const beginWidth = centerWidth - (size / 2);
        return img.slice(
            [beginHeight, beginWidth, 0], [size, size, 3]
        );
    }

    adjustVideoSize(width, height) {
        const aspectRatio = width / height;
        if(width >= height) {
            this.webcamElement.width = aspectRatio * this.webcamElement.height;
        } else if(width < height) {
            this.webcamElement.height = this.webcamElement.width / aspectRatio;
        }
    }

    async setup() {
        return new Promise((resolve, reject) => {
            navigator.getUserMedia = navigator.getUserMedia || 
                navigator.webkitGetUserMedia || navigator.mozGetUserMedia || 
                navigator.msGetUserMedia;

            if(navigator.getUserMedia) {
                navigator.getUserMedia({
                    video: {width: 224, height: 224}
                }, stream => {
                    this.webcamElement.srcObject = stream;
                    this.webcamElement.addEventListener('loadeddata', async () => {
                        this.adjustVideoSize(
                            this.webcamElement.videoWidth,
                            this.webcamElement.videoHeight
                        );
                        resolve();
                    }, false);
                }, error => {
                    reject(error);
                });
            } else {
                reject();
            }
        });
    }
}