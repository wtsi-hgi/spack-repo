# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVarband(RPackage):
	"""Variable Banding of Large Precision Matrices

	Implementation of the variable banding procedure for modeling local dependence and estimating precision matrices that is introduced in Yu & Bien (2016) and is available at <https://arxiv.org/abs/1604.07451>.
	"""
	
	homepage = "http://github.com/hugogogo/varband"
	cran = "varband" 

	version("0.9.0", md5="2ec6043322a640dacb7aefa563a004c0")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
