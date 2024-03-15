# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCheapr(RPackage):
	"""Simple Functions to Save Time and Memory

	Fast and memory-efficient (or 'cheap') tools to facilitate
    efficient programming, saving time and memory. It aims to provide
    'cheaper' alternatives to common base R functions, as well as some
    additional functions.
	"""
	
	cran = "cheapr" 

	version("0.2.0", md5="3f2ff7173f6087ab4a7bae1e019f1572")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-collapse@2:", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
