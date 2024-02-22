# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWacolors(RPackage):
	"""Colorblind-Friendly Palettes from Washington State

	Color palettes taken from the landscapes and cities of Washington 
    state. Colors were extracted from a set of photographs, and then combined to 
    form a set of continuous and discrete palettes.  Continuous palettes were 
    designed to be perceptually uniform, while discrete palettes were chosen to
    maximize contrast at several different levels of overall brightness and 
    saturation. Each palette has been evaluated to ensure colors are 
    distinguishable by colorblind people.
	"""
	
	homepage = "https://github.com/CoryMcCartan/wacolors"
	cran = "wacolors" 

	version("0.3.1", md5="264417791d2bac95a61df21ba9f0f54b")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
