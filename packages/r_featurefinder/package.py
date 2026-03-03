# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFeaturefinder(RPackage):
	"""Feature Finder

	Finds modelling features through a detailed analysis of model residuals using 'rpart' classification and regression trees. Scans the residuals of a model across subsets of the data to identify areas where the model prediction differs from the actual target variable. S. Chatterjee, A. S. Hadi (2006) <doi:10.1002/0470055464>.
	"""
	
	cran = "featurefinder" 

	version("1.1", md5="4070aa75286c4183893b74d62e9b9c83")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-rpart-plot", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
