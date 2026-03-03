# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForge(RPackage):
	"""Casting Values into Shape

	Helper functions with a consistent interface to coerce and verify
    the types and shapes of values for input checking.
	"""
	
	cran = "forge" 

	version("0.2.0", md5="4078784d52bb5d072ed2b44beaa72111")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-rlang@0.3.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
