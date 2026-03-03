# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RColorist(RPackage):
	"""Coloring Wildlife Distributions in Space-Time

	Color and visualize wildlife distributions in
    space-time using raster data. In addition to enabling display of
    sequential change in distributions through the use of small multiples,
    'colorist' provides functions for extracting several features of
    interest from a sequence of distributions and for visualizing those
    features using HCL (hue-chroma-luminance) color palettes. Resulting
    maps allow for "fair" visual comparison of intensity values (e.g.,
    occurrence, abundance, or density) across space and time and can be
    used to address questions about where, when, and how consistently a
    species, group, or individual is likely to be found.
	"""
	
	homepage = "https://github.com/mstrimas/colorist"
	cran = "colorist" 

	version("0.1.2", md5="abb8658c34c5fd272b5a5d14ee78e292")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
