# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPerc(RPackage):
	"""Using Percolation and Conductance to Find Information Flow
Certainty in a Direct Network

	To find the certainty of dominance interactions with indirect
    interactions being considered.
	"""
	
	cran = "Perc" 

	version("0.1.6", md5="e61d55af0bc6dfca75bb4c8b239b1e10")

	depends_on("r@2.14:", type=("build", "run"))
