# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFeatureterminator(RPackage):
	"""Feature Selection Engine to Remove Features with Minimal
Predictive Power

	The aim is to take in data.frame inputs and utilises methods, such as recursive feature engineering, to enable the features to be removed.
    What this does differently from the other packages, is that it gives you the choice to remove the variables manually, or it automated this process.
    Feature selection is a concept in machine learning, and statistical pipelines, whereby unimportant, or less predictive variables are eliminated from the analysis, see Boughaci (2018) <doi:10.1007/s40595-018-0107-y>. 
	"""
	
	cran = "FeatureTerminatoR" 

	version("1.0.0", md5="26f6dd23ad9432d0a8641e026e40f0db")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
