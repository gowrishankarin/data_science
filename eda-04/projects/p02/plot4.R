new_scc <- SCC[grep("Coal*", SCC$EI.Sector),]

new_nei <- filter(NEI, SCC == new_scc$SCC)

return(new_nei)