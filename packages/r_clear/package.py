# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClear(RPackage):
	"""Clean the R Console and Environment

	Small package to clean the R console and the R environment
    with the call of just one function.
	"""
	
	homepage = "https://github.com/joundso/cleaR"
	cran = "cleaR" 

	version("0.0.4", md5="c8f53d973ff7937c802fb136086be4f9")

	depends_on("r@3.1:", type=("build", "run"))
