# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNvar(RPackage):
	"""Nonlinear Vector Autoregression Models

	Estimate nonlinear vector autoregression models (also known as the 
    next generation reservoir computing) for nonlinear dynamic systems. The 
    algorithm was described by Gauthier et al. (2021) <doi:10.1038/s41467-021-25801-2>.
	"""
	
	homepage = "https://github.com/Sciurus365/NVAR"
	cran = "NVAR" 

	version("0.1.0", md5="8e64af407198affc4a526c3c2843540c")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
