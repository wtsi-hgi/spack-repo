# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcolorconesa(RPackage):
	"""Conesa Colors Palette

	Provides a collection of palettes designed to integrate with 'ggplot', reflecting the color schemes associated with 'ConesaLab'.
	"""
	
	cran = "RColorConesa" 

	version("1.0.0", md5="f917e2999f583e86e1b4e7e54b20897a")

	depends_on("r-ggplot2", type=("build", "run"))
