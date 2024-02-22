# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpisemble(RPackage):
	"""Ensemble Based Machine Learning Approach for Predicting
Methylation States

	DNA methylation (6mA) is a major epigenetic process by which alteration in gene expression took place without changing the DNA sequence. Predicting these sites in-vitro is laborious, time consuming as well as costly. This 'EpiSemble' package is an in-silico pipeline for predicting DNA sequences containing the 6mA sites. It uses an ensemble-based machine learning approach by combining Support Vector Machine (SVM), Random Forest (RF) and Gradient Boosting approach to predict the sequences with 6mA sites in it. This package has been developed by using the concept of Chen et al. (2019) <doi:10.1093/bioinformatics/btz015>.
	"""
	
	cran = "EpiSemble" 

	version("0.1.1", md5="3ff0bdc3e661ac9c8a16cb424583fd42")

	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-splitstackshape", type=("build", "run"))
	depends_on("r-entropy", type=("build", "run"))
	depends_on("r-party", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ftrcool", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
