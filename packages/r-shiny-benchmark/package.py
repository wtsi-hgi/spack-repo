# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyBenchmark(RPackage):
	"""Benchmark the Performance of 'shiny' Applications

	Compare performance between different versions of a 'shiny' application based on 'git' references.
	"""
	
	homepage = "https://github.com/Appsilon/shiny.benchmark"
	cran = "shiny.benchmark" 

	version("0.1.1", md5="2cf49540f99c5a06e997acd2ecf9903a")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-renv", type=("build", "run"))
	depends_on("r-shinytest2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
