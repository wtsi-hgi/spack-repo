# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesroe(RPackage):
	"""Bayesian Regions of Evidence

	Computation and visualization of Bayesian Regions of Evidence to 
    systematically evaluate the sensitivity of a superiority or non-inferiority 
    claim against any prior assumption of its assessors. Methodological details 
    are elaborated by Hoefler and Miller (2023) <https://osf.io/jxnsv>. 
    Besides generic functions, the package also provides an intuitive 'Shiny' 
    application, that can be run in local R environments.
	"""
	
	homepage = "https://github.com/waidschrat/bayesROE"
	cran = "bayesROE" 

	version("0.1", md5="de91b28943570233a5a5c17a8c02e708")

	depends_on("r-colourpicker", type=("build", "run"))
	depends_on("r-config@0.3.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-golem@0.3.3:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-shiny@1.7.2:", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
