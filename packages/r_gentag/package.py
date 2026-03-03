# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGentag(RPackage):
	"""Generate Color Tag Sequences

	Implement a coherent and flexible protocol for animal color tagging. 'GenTag' provides a simple computational routine with low CPU usage to create color sequences for animal tag. First, a single-color tag sequence is created from an algorithm selected by the user, followed by verification of the combination uniqueness. Three methods to produce color tag sequences are provided. Users can modify the main function core to allow a wide range of applications. 
	"""
	
	cran = "GenTag" 

	version("1.0", md5="222c06c23fd17f13b9cf4bef7a29fed9")

	depends_on("r@3.5:", type=("build", "run"))
