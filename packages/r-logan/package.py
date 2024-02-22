# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLogan(RPackage):
	"""Log File Analysis in International Large-Scale Assessments

	Enables users to handle the dataset cleaning for conducting
    specific analyses with the log files from two international educational
    assessments: the Programme for International Student Assessment (PISA,
    <https://www.oecd.org/pisa/>) and the Programme for the International
    Assessment of Adult Competencies (PIAAC,
    <https://www.oecd.org/skills/piaac/>). An illustration of the analyses can be
    found on the LOGAN Shiny app (<https://loganpackage.shinyapps.io/shiny/>) on
    your browser.
	"""
	
	cran = "LOGAN" 

	version("1.0.1", md5="9dcad11dd8f569dd0740a6adb4a4b1e4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-pander@0.6.1:", type=("build", "run"))
	depends_on("r-psych@1.7.8:", type=("build", "run"))
	depends_on("r-foreign@0.8.69:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-modules", type=("build", "run"))
