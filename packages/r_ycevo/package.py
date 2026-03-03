# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYcevo(RPackage):
	"""Nonparametric Estimation of the Yield Curve Evolution

	Nonparametric estimation of the discount rate and yield curve. 
    Koo, B., La Vecchia, D., & Linton, O. B. (2021) <doi:10.1016/j.jeconom.2020.04.014> 
    describe the application with the Center for Research in Security Prices (CRSP) Bond Data 
    and document the methods of this package.
	"""
	
	homepage = "https://github.com/bonsook/ycevo"
	cran = "ycevo" 

	version("0.1.2", md5="9005def8d436f42a0570e3baca51fe55")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
