# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSfc(RPackage):
	"""Substance Flow Computation

	Provides a function sfc() to compute the substance flow
    with the input files --- "data" and "model". If sample.size is
    set more than 1, uncertainty analysis will be executed while
    the distributions and parameters are supplied in the file "data".
	"""
	
	homepage = "https://github.com/ctfysh/sfc"
	cran = "sfc" 

	version("0.1.0", md5="bdb54c60d2f9a6918abdce023a1bc0a9")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-triangle", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
