# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBasetheme(RPackage):
	"""Themes for Base Graphics Plots

	Functions to create and select graphical themes for the base plotting system. Contains: 1) several custom pre-made themes 2) mechanism for creating new themes by making persistent changes to the graphical parameters of base plots.
	"""
	
	homepage = "https://github.com/karoliskoncevicius/basetheme"
	cran = "basetheme" 

	version("0.1.3", md5="851c5b0c2ff5d89c5605dca034a61e42")

	depends_on("r@3.2.2:", type=("build", "run"))
