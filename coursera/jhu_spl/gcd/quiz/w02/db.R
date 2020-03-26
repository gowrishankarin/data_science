github <- function() {
    library(httr)
    oauth_endpoints("github")
    
    myapp <- oauth_app("github", "e20e84efeb09ef645c3a", secret="2535edf01f5b35f7022a580b0adb0a0763d9a41c")
    
    github_token <- oauth2.0_token(oauth_endpoints("github"), myapp)
    
    gtoken <- config(token = github_token)
    
    req <- GET("https://api.github.com/users/jtleek/repos", gtoken)
    
    stop_for_status(req)
    
    content(req)
}