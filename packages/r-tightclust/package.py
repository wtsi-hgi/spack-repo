# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTightclust(RPackage):
	"""Tight Clustering

	The functions needed to perform tight clustering Algorithm.
	"""
	
	cran = "tightClust" 

	version("1.1", md5="c9453c1ecdbc4e0a5abb06601b95d5de")

	depends_on("r@2.10.1:", type=("build", "run"))
