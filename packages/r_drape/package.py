# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrape(RPackage):
	"""Doubly Robust Average Partial Effects

	Doubly robust average partial effect estimation. This implementation contains methods for adding additional smoothness to plug-in regression procedures and for estimating score functions using smoothing splines. Details of the method can be found in Harvey Klyne and Rajen D. Shah (2023) <arXiv:2308.09207>.
	"""
	
	cran = "drape" 

	version("0.0.1", md5="e5a3582435bbd1bdf82e8e7670a3fe3a")

