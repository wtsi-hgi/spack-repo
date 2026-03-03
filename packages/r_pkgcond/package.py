# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPkgcond(RPackage):
	"""Classed Error and Warning Conditions

	This provides utilities for creating classed error and warning
  conditions based on where the error originated.
	"""
	
	homepage = "https://github.com/RDocTaskForce/pkgcond"
	cran = "pkgcond" 

	version("0.1.1", md5="75c26f7350cfb41e66cbe40d1a7c3ee3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
