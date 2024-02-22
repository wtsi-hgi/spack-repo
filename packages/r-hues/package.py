# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHues(RPackage):
	"""Distinct Colour Palettes Based on 'iwanthue'

	Creating effective colour palettes for figures is 
    challenging. This package generates and plot palettes of optimally 
    distinct colours in perceptually uniform colour space, based on 
    'iwanthue' <http://tools.medialab.sciences-po.fr/iwanthue/>. 
    This is done through k-means clustering of CIE Lab colour space, 
    according to user-selected constraints on hue, chroma, and 
    lightness.
	"""
	
	homepage = "https://github.com/johnbaums/hues"
	cran = "hues" 

	version("0.2.0", md5="535023c47c512cd69f5d504cebd77625")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
