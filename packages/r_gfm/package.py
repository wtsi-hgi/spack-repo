# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGfm(RPackage):
	"""Generalized Factor Model

	Generalized factor model is implemented for ultra-high dimensional data with mixed-type variables.
    Two algorithms, variational EM and alternate maximization, are designed to implement the generalized factor model,
    respectively. The factor matrix and loading matrix together with the number of factors can be well estimated. 
    This model can be employed in social and behavioral sciences, economy and finance, and  genomics, 
    to extract interpretable nonlinear factors. More details can be referred to 
    Wei Liu, Huazhen Lin, Shurong Zheng and Jin Liu. (2021) <doi:10.1080/01621459.2021.1999818>. 
	"""
	
	homepage = "https://github.com/feiyoung/GFM"
	cran = "GFM" 

	version("1.2.1", md5="c36eb14af6e6e9a8bdd2c986b5b07fd8")

	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
