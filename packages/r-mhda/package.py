# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMhda(RPackage):
	"""Massive Hierarchically Data Analysis

	Three main functions about analyzing massive data (missing observations are allowed) considered from multiple layers of categories.
	"""
	
	cran = "MHDA" 

	version("1.2", md5="6d6578d9790259b3bbcea47d3f0f5a77")

