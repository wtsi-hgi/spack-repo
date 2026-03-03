# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirt(RPackage):
	"""Multidimensional Item Response Theory

	Analysis of discrete response data using
    unidimensional and multidimensional item analysis models under the Item
    Response Theory paradigm (Chalmers (2012) <doi:10.18637/jss.v048.i06>). 
    Exploratory and confirmatory item factor analysis models
	are estimated with quadrature (EM) or stochastic (MHRM) methods. Confirmatory
    bi-factor and two-tier models are available for modeling item testlets using
	dimension reduction EM algorithms, while multiple group analyses and 
	mixed effects designs are included for detecting differential item, bundle, 
	and test functioning, and for modeling item and person covariates. 
	Finally, latent class models such as the DINA, DINO, multidimensional latent class, 
	mixture, and zero-inflated response models are supported.
	"""
	
	homepage = "https://github.com/philchalmers/mirt"
	cran = "mirt" 

	version("1.41", md5="5356320bad981f0ad0047890df52ecc0")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-gparotation", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-matrix@1.5.0:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-deriv", type=("build", "run"))
	depends_on("r-pbapply@1.3.0:", type=("build", "run"))
	depends_on("r-dcurver", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
