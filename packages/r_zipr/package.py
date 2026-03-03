# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZipr(RPackage):
	"""Pythonic Zip() for R

	Implements Python-style zip for R. Is a more flexible version of cbind.
	"""
	
	homepage = "https://github.com/leslie-huang/zipR"
	cran = "zipR" 

	version("0.1.1", md5="cc2ca4be4624f3994ee477a8ea070d9d")

	depends_on("r@2.1:", type=("build", "run"))
