# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIimi(RPackage):
	"""Identifying Infection with Machine Intelligence

	A novel machine learning method for plant viruses diagnostic using 
    genome sequencing data. This package includes three different machine 
    learning models, random forest, XGBoost, and elastic net, to train and 
    predict mapped genome samples. Mappability profile and unreliable regions 
    are introduced to the algorithm, and users can build a mappability profile 
    from scratch with functions included in the package. Plotting mapped sample 
    coverage information is provided.
	"""
	
	cran = "iimi" 

	version("1.0.2", md5="64086005de287eb93358781eeab37396")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-mltools", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-mtps", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
