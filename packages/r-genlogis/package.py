# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenlogis(RPackage):
	"""Generalized Logistic Distribution

	Provides basic distribution functions for a generalized logistic distribution proposed by Rathie and Swamee (2006) <https://www.rroij.com/open-access/on-new-generalized-logistic-distributions-and-applicationsbarreto-fhs-mota-jma-and-rathie-pn-.pdf>. It also has an interactive 'RStudio' plot for better guessing dynamically of initial values for ease of included optimization and simulating.
	"""
	
	homepage = "https://pinduzera.github.io/genlogis/"
	cran = "genlogis" 

	version("1.0.2", md5="46a9d2afdc795e65cf1823d66fb78457")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-distr", type=("build", "run"))
	depends_on("r-manipulate", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
