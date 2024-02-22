# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiascorrector(RPackage):
	"""A GUI to Correct Measurement Bias in DNA Methylation Analyses

	A GUI to correct measurement bias in DNA methylation
    analyses. The 'BiasCorrector' package just wraps the functions
    implemented in the 'R' package 'rBiasCorrection' into a shiny web
    application in order to make them more easily accessible. Publication:
    Kapsner et al. (2021) <doi:10.1002/ijc.33681>.
	"""
	
	homepage = "https://github.com/kapsner/BiasCorrector"
	cran = "BiasCorrector" 

	version("0.2.2", md5="e980bd5e0a7916f60c46add086d942bf")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rbiascorrection@0.3.4:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
