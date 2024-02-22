# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLfapp(RPackage):
	"""Shiny Apps for Lateral Flow Assays

	Shiny apps for the quantitative analysis of images from lateral flow assays (LFAs). The images are segmented and background corrected and color intensities are extracted. The apps can be used to import and export intensity data and to calibrate LFAs by means of linear, loess, or gam models. The calibration models can further be saved and applied to intensity data from new images for determining concentrations.
	"""
	
	homepage = "https://github.com/fpaskali/LFApp"
	cran = "LFApp" 

	version("1.4", md5="e963c682ac356b783bcd3a60dc5ef6e8")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-shinyfiles", type=("build", "run"))
	depends_on("r-shinymobile@0.9:", type=("build", "run"))
	depends_on("r-ebimage", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
