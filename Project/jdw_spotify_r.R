setwd("C:/Users/jorda/OneDrive/Python_Camp/python_summer2021/Project")
library(tidyverse)
library(RColorBrewer)

dat <- read.csv("campaignsongs.csv")

head(dat)
summary(dat)

dat["Key"][dat["Key"] == 0] <- "C"
dat["Key"][dat["Key"] == 1] <- "C\U266F"
dat["Key"][dat["Key"] == 2] <- "D"
dat["Key"][dat["Key"] == 3] <- "E\U266D"
dat["Key"][dat["Key"] == 4] <- "E"
dat["Key"][dat["Key"] == 5] <- "F"
dat["Key"][dat["Key"] == 6] <- "F\U266F"
dat["Key"][dat["Key"] == 7] <- "G"
dat["Key"][dat["Key"] == 8] <- "A\U266D"
dat["Key"][dat["Key"] == 9] <- "A"
dat["Key"][dat["Key"] == 10] <- "B\U266D"
dat["Key"][dat["Key"] == 11] <- "B"

biden <- dat[dat$Playlist == "Biden",]
trump <- dat[dat$Playlist == "Trump",]


fig1 <- ggplot(data = dat, aes(x = Danceability, fill = Playlist, color = Playlist)) +
  scale_fill_manual(values = c("blue", "red")) +
  scale_color_manual(values = c("black", "black")) +
  geom_histogram(binwidth = 0.01, alpha = 0.8) +
  geom_density(alpha = 0.2) +
  labs(y = "", title = "Figure 1: Danceability of 2020 Presidential Campaign Playlists",
       subtitle = "Courtesy of Spotify and the New York Times") +
  theme_minimal()
fig1

fig2 <- ggplot(data = dat, aes(x = Energy, fill = Playlist, color = Playlist)) +
  scale_fill_manual(values = c("blue", "red")) +
  scale_color_manual(values = c("black", "black")) +
  geom_histogram(binwidth = 0.01, alpha = 0.8) +
  geom_density(alpha = 0.2) +
  labs(y = "", title = "Figure 2: Energy of 2020 Presidential Campaign Playlists",
       subtitle = "Courtesy of Spotify and the New York Times") +
  theme_minimal()
fig2

fig3 <- ggplot(data = dat, aes(x = Key, y = (..count..)/sum(..count..), fill = Playlist, color = Playlist)) +
  geom_bar(position = 'dodge') +
  scale_fill_manual(values = c("blue", "red")) +
  scale_color_manual(values = c("black", "black")) +
  coord_polar(theta = "x", start = 10.15) +
  labs(y = "",
       title = "Figure 3: Key Signatures of 2020 Presidential Campaign Playlists",
       subtitle = "Proportion of Playlist Songs in Each Key",
       caption = "Playlists courtesy of the New York Times and the Spotify API") +
  theme_bw()
fig3

ggsave("fig3.png", fig3)
