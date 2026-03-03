# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBwimage(RPackage):
	"""Describe Image Patterns in Natural Structures

	A computational tool to describe patterns in black and white images from natural structures. 'bwimage' implemented functions for exceptionally broad subject. For instance, 'bwimage' provide examples that range from calculation of canopy openness, description of patterns in vertical vegetation structure, to patterns in bird nest structure.   
	"""
	
	cran = "bwimage" 

	version("1.3", md5="b5809acf871a5662e78a0b959e3bb36b")

	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
