# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPainter(RPackage):
	"""Creation and Manipulation of Color Palettes

	Functions for creating color palettes, visualizing
    palettes, modifying colors, and assigning colors for plotting.
	"""
	
	cran = "painter" 

	version("0.1.0", md5="29d8d68b0ab07bd89bebdf8237fc0290")

