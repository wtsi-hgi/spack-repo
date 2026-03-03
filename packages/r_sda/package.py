# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSda(RPackage):
	"""Shrinkage Discriminant Analysis and CAT Score Variable Selection

	Provides an efficient framework for 
   high-dimensional linear and diagonal discriminant analysis with 
   variable selection.  The classifier is trained using James-Stein-type 
   shrinkage estimators and predictor variables are ranked using 
   correlation-adjusted t-scores (CAT scores).  Variable selection error 
   is controlled using false non-discovery rates or higher criticism.
	"""
	
	homepage = "https://strimmerlab.github.io/software/sda/"
	cran = "sda" 

	version("1.3.8", md5="c3ed1f2feb41061b625af70b84bf98b7")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-entropy@1.3.1:", type=("build", "run"))
	depends_on("r-corpcor@1.6.10:", type=("build", "run"))
	depends_on("r-fdrtool@1.2.17:", type=("build", "run"))
