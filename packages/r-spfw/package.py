# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpfw(RPackage):
	"""Hierarchical Spatial Finlay-Wilkinson Model

	Estimation and Prediction Functions Using Bayesian Hierarchical Spatial Finlay-Wilkinson Model for Analysis of Multi-Environment Field Trials.
	"""
	
	cran = "spFW" 

	version("0.1.0", md5="8bae42e20427303a3e151119c538b654")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("fftw", type=("build", "link", "run"))
