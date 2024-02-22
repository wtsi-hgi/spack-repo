# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RD2mcs(RPackage):
	"""Data Driving Multiple Classifier System

	
        Provides a novel framework to able to automatically develop and deploy
    an accurate Multiple Classifier System based on the feature-clustering 
    distribution achieved from an input dataset. 'D2MCS' was developed focused on 
    four main aspects: (i) the ability to determine an effective method to 
    evaluate the independence of features, (ii) the identification of the 
    optimal number of feature clusters, (iii) the training and tuning of ML 
    models and (iv) the execution of voting schemes to combine the outputs of 
    each classifier comprising the Multiple  Classifier System.
	"""
	
	homepage = "https://github.com/drordas/D2MCS"
	cran = "D2MCS" 

	version("1.0.1", md5="dfd3505e06a86dd1b17e1b747c82ed13")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fselector", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-infotheo", type=("build", "run"))
	depends_on("r-mccr", type=("build", "run"))
	depends_on("r-mltools", type=("build", "run"))
	depends_on("r-modelmetrics", type=("build", "run"))
	depends_on("r-questionr", type=("build", "run"))
	depends_on("r-recipes", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-tictoc", type=("build", "run"))
	depends_on("r-varhandle", type=("build", "run"))
