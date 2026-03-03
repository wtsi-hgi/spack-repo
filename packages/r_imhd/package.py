# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImhd(RPackage):
	"""Artificial Intelligence Based Machine Learning Algorithms for
Height Diameter Relationships of Conifer Trees

	Estimating height of forest plant is one of the key challenges of recent times. This package will help to fit and validate AI (Artificial Intelligence) based machine learning algorithms for estimation of height of conifer trees based on diameter at breast height as explanatory variable using algorithm of Paul et al. (2022) <doi:10.1371/journal.pone.0270553>..
	"""
	
	cran = "ImHD" 

	version("0.1.0", md5="8988fe0b75f2bdf3aa168e9771327d3f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
