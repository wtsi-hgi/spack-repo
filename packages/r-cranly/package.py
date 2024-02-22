# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCranly(RPackage):
	"""Package Directives and Collaboration Networks in CRAN

	Core visualizations and summaries for the CRAN package database. The package provides comprehensive methods for cleaning up and organizing the information in the CRAN package database, for building package directives networks (depends, imports, suggests, enhances, linking to) and collaboration networks, producing package dependence trees, and for computing useful summaries and producing interactive visualizations from the resulting networks and summaries. The resulting networks can be coerced to 'igraph' <https://CRAN.R-project.org/package=igraph> objects for further analyses and modelling.
	"""
	
	homepage = "https://github.com/ikosmidis/cranly"
	cran = "cranly" 

	version("0.6.0", md5="764ac7f6f154a0268f15bc523b959ebf")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-countrycode", type=("build", "run"))
	depends_on("r-wordcloud", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
