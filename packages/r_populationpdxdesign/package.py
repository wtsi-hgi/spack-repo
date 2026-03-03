# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPopulationpdxdesign(RPackage):
	"""Designing Population PDX Studies

	Run simulations to assess the impact of various designs features
    and the underlying biological behaviour on the outcome of a Patient Derived
    Xenograft (PDX) population study. This project can either be deployed to a
    server as a 'shiny' app or installed locally as a package and run the app
    using the command 'populationPDXdesignApp()'.
	"""
	
	cran = "populationPDXdesign" 

	version("1.0.3", md5="ac1102fec1d5d65ac622947b20705ec5")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-roxygen2", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
