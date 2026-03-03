# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBinda(RPackage):
	"""Multi-Class Discriminant Analysis using Binary Predictors

	Implements functions for multi-class
   discriminant analysis using binary predictors, for corresponding 
   variable selection, and for dichotomizing continuous data.
	"""
	
	homepage = "https://strimmerlab.github.io/software/binda/"
	cran = "binda" 

	version("1.0.4", md5="1d3ca1fb798a8c4320c6f284f24e80ad")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-entropy@1.3.1:", type=("build", "run"))
