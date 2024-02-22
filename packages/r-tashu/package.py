# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTashu(RPackage):
	"""Analysis and Prediction of Bicycle Rental Amount

	Provides functions for analyzing citizens' bicycle usage pattern and predicting rental amount on specific conditions.
    Functions on this package interacts with data on 'tashudata' package, a 'drat' repository.
    'tashudata' package contains rental/return history on public bicycle system('Tashu'), weather for 3 years and bicycle station information. 
    To install this data package, see the instructions at <https://github.com/zeee1/Tashu_Rpackage>.
    top10_stations(), top10_paths() function visualizes image showing the most used top 10 stations and paths.
    daily_bike_rental() and monthly_bike_rental() shows daily, monthly amount of bicycle rental.
    create_train_dataset(), create_test_dataset() is data processing function for prediction.
    Bicycle rental history from 2013 to 2014 is used to create training dataset and that on 2015 is for test dataset.
    Users can make random-forest prediction model by using create_train_model() 
    and predict amount of bicycle rental in 2015 by using predict_bike_rental().
	"""
	
	cran = "tashu" 

	version("0.1.1", md5="391c91fc0e0439e60d1e5c818398fbde")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-drat", type=("build", "run"))
