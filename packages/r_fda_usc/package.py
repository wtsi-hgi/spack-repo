# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdaUsc(RPackage):
	"""Functional Data Analysis and Utilities for Statistical Computing

	Routines for exploratory and descriptive analysis of functional data such as depth measurements, atypical curves detection, regression models, supervised classification, unsupervised classification and functional analysis of variance.
	"""
	
	homepage = "https://github.com/moviedo5/fda.usc"
	cran = "fda.usc" 

	version("2.1.0", md5="5e65e335ca5951d30e8c862a33952a58")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ksamples", type=("build", "run"))
