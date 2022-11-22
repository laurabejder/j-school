require("readr")
require("ggplot2")
require("esquisse")
require("tidyverse")

setwd('~/Desktop/GitHub/j-school/reporting_II/learning_R')

housing_df = read_csv('housing_data.csv')

#esquisser(viewer='browser')

# Here I just copied the code from equisser - nice function!
library(ggplot2)

ggplot(housing_df) +
 aes(x = pct_black_and_hispanic, y = pct_below_poverty, colour = evictions_per_thousand_ppl, 
 size = population) +
 geom_point(shape = "circle") +
 scale_color_distiller(palette = "YlOrRd", direction = 1) +
 theme_minimal() +
 facet_wrap(vars(borough))

# And here I write it myself - just for practice - shouldn't be used for analysis!!
# Not population adjusted!

ggplot(housing_df, aes(x=violations, y=evictions)) + 
  geom_point(size=1.5, color='orange') +
  facet_wrap(~borough) +
  stat_smooth(method='lm') +
  coord_cartesian(xlim = c(0, 1400), ylim = c(0, 800)) +
  theme_minimal() +
  labs(
    x = 'evictions',
    y = 'housing violations',
    title = 'Zipcodes with more housing violations also have more evictions',
    subtitle = 'Housing violations vs evictions in NYC by zipcode'
  )

















