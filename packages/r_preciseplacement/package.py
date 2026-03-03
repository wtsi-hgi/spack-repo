# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPreciseplacement(RPackage):
	"""Suite of Functions to Help Get Plot Elements Exactly Where You
Want Them

	Provides a selection of tools that make it easier to place elements onto a (base R) plot exactly where you want them. It allows users to identify points and distances on a plot in terms of inches, pixels, margin lines, data units, and proportions of the plotting space, all in a manner more simple than manipulating par().
	"""
	
	cran = "precisePlacement" 

	version("0.1.0", md5="f1fb419d061e3de2e1af58e7b9f1f04e")

