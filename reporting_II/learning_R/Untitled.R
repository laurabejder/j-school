require("readr")
require("ggplot2")
require("esquisse")
require("tidyverse")

setwd('~/Desktop')

housing_df = read_csv('housing_data.csv')

esquisser(viewer='browser')

# Here I just copied the code from equisser - nice function!
library(ggplot2)

ggplot(housing_df) +
 aes(x = pct_black_and_hispanic, y = pct_below_poverty, colour = evictions_per_thousand_ppl, 
 size = population) +
 geom_point(shape = "circle") +
 scale_color_distiller(palette = "YlOrRd", direction = 1) +
 theme_minimal() +
 facet_wrap(vars(borough))
