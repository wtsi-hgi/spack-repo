# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlamlasso(RPackage):
	"""Penalization in Large Scale Generalized Linear Array Models

	Efficient design matrix free  lasso penalized estimation in large scale 2 and 3-dimensional generalized linear array model framework. The procedure is based on the gdpg algorithm from Lund et al. (2017) <doi:10.1080/10618600.2017.1279548>. Currently Lasso or Smoothly Clipped Absolute Deviation (SCAD) penalized estimation is possible for the following models: The Gaussian model with identity link, the Binomial model with logit link, the Poisson model with log link and the Gamma model with log link. It is also possible to include a  component in the model with non-tensor design e.g an intercept. Also provided are functions, glamlassoRR() and glamlassoS(), fitting special cases of GLAMs. 
	"""
	
	cran = "glamlasso" 

	version("3.0.1", md5="5f1780a1406cd9ef0385e26bffd9d935")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
