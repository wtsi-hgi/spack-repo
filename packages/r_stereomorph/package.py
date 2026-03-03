# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStereomorph(RPackage):
	"""Stereo Camera Calibration and Reconstruction

	Functions for the collection of 3D points and curves using a stereo camera setup.
	"""
	
	homepage = "https://aaronolsen.github.io/software/stereomorph.html"
	cran = "StereoMorph" 

	version("1.6.7", md5="6399f03b4525026aae0322eedab2f593")

	depends_on("r@2.11:", type=("build", "run"))
	depends_on("r-bezier@1.1:", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-shiny@0.13:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-tiff", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-svgviewr@1.0.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
