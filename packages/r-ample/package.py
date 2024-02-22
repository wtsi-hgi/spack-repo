# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmple(RPackage):
	"""Shiny Apps to Support Capacity Building on Harvest Control Rules

	Three Shiny apps are provided that introduce Harvest Control Rules (HCR) for fisheries management.
    'Introduction to HCRs' provides a simple overview to how HCRs work. Users are able to select their own HCR and
    step through its performance, year by year. Biological variability and estimation uncertainty are introduced.
    'Measuring performance' builds on the previous app and introduces the idea of using performance indicators
    to measure HCR performance.
    'Comparing performance' allows multiple HCRs to be created and tested, and their performance compared so that the
    preferred HCR can be selected.
	"""
	
	homepage = "https://github.com/PacificCommunity/ofp-sam-ample"
	cran = "AMPLE" 

	version("1.0.2", md5="04c91ffda54c8b55c95a4db7e51b5a92")

	depends_on("r-shiny@1.7.3:", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-r6@2.5.1:", type=("build", "run"))
	depends_on("r-scales@1.2.1:", type=("build", "run"))
	depends_on("r-shinyjs@2.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-shinyscreenshot@0.2:", type=("build", "run"))
