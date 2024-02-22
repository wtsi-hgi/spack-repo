# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpo(RPackage):
	"""Enhanced Portfolio Optimization (EPO)

	Implements the Enhanced Portfolio Optimization (EPO) method as 
    described in Pedersen, Babu and Levine (2021)
    <doi:10.2139/ssrn.3530390>.
	"""
	
	homepage = "https://github.com/Reckziegel/epo"
	cran = "epo" 

	version("0.1.0", md5="0687b1bfb5648c1dab13d7ee02972ab4")

	depends_on("r-assertthat@0.2.1:", type=("build", "run"))
	depends_on("r-dplyr@1.1.2:", type=("build", "run"))
	depends_on("r-rlang@1.1.1:", type=("build", "run"))
	depends_on("r-xts@0.13.1:", type=("build", "run"))
