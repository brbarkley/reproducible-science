import recipy
import importlib
import os

os.chdir('C:\\Users\\d1brb03\\Documents\\Workshops\\reproducible-science')

# NOTE: Import modules
subset = importlib.import_module('.data.01_subset-data-GBP', 'src')
plotwines = importlib.import_module('.visualization.02_visualize-wines', 'src')
country_sub = importlib.import_module('.data.03_country-subset', 'src')

# NOTE: Run analysis
subset.process_data_GBP('data/raw/winemag-data-130k-v2.csv')
plotwines.create_plots('data/interim/2018-05-09-winemag_priceGBP.csv')
country_sub.get_country('data/interim/2018-05-09-winemag_priceGBP.csv',
                       'Chile')
