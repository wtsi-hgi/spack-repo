# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVolcanoplot(RPackage):
	"""Volcano Plot for Clinical Trial Adverse Events

	Interactive adverse event (AE) volcano plot for monitoring clinical trial safety. This tool allows users to view the overall distribution of AEs in a clinical trial using standard (e.g. MedDRA preferred term) or custom (e.g. Gender) categories using a volcano plot similar to proposal by Zink et al. (2013) <doi:10.1177/1740774513485311>. This tool provides a stand-along shiny application and flexible shiny modules allowing this tool to be used as a part of more robust safety monitoring framework like the Shiny app from the 'safetyGraphics' R package. 
	"""
	
	cran = "volcanoPlot" 

	version("1.0.0", md5="9dce0fcc4ee4cfd36070828a4d414887")

	depends_on("r-fmsb", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
