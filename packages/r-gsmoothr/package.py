# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsmoothr(RPackage):
	"""Smoothing tools

	Tools rewritten in C for various smoothing tasks
	"""
	
	cran = "gsmoothr" 

	version("0.1.7", md5="d90da237ee71eb665b8d59f210c5b6ee")

	depends_on("r@2.8:", type=("build", "run"))
