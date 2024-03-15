# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROeli(RPackage):
	"""My Utilities for Developing Data Science Software

	Some general helper functions that I and maybe others find useful 
    when developing data science software. Functionality includes argument 
    validation, density calculation, sampling, matrix printing, user 
    interaction, storage helpers and more. The vignettes illustrate use cases.
	"""
	
	homepage = "https://github.com/loelschlaeger/oeli"
	cran = "oeli" 

	version("0.4.1", md5="5f57e9d6a5d9ac6690fe2b46514841c7")

	depends_on("r-benchmarkme", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-hexsticker", type=("build", "run"))
	depends_on("r-latex2exp", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rprojroot", type=("build", "run"))
	depends_on("r-showtext", type=("build", "run"))
	depends_on("r-sysfonts", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
