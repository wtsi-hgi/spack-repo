# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNormalityassessment(RPackage):
	"""A Graphical User Interface for Testing Normality Visually

	Package including an interactive Shiny application for
    testing normality visually.
	"""
	
	homepage = "https://github.com/ccasement/NormalityAssessment"
	cran = "NormalityAssessment" 

	version("0.1.0", md5="22bfddc52e54bc96255a16020b2f2678")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@1.0.7:", type=("build", "run"))
	depends_on("r-dt@0.19:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-rio@0.5.27:", type=("build", "run"))
	depends_on("r-rmatio@0.16:", type=("build", "run"))
	depends_on("r-shiny@1.7.1:", type=("build", "run"))
	depends_on("r-shinyalert@2:", type=("build", "run"))
	depends_on("r-shinybs@0.61:", type=("build", "run"))
	depends_on("r-stringi@1.7.4:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
