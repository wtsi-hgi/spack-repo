# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJadelizardoptions(RPackage):
	"""Trading Jade Lizard Option Strategies

	Jade Lizard and Reverse Jade Lizard Option Strategies are presented here through their Graphs. The graphic indicators, strategies, calculations, functions and all the discussions are for academic, research, and educational purposes only and should not be construed as investment advice and come with absolutely no Liability.
    Russell A. Stultz (“The option strategy desk reference: an essential reference for option traders (First edition.)”, 2019, ISBN: 9781949443912).
	"""
	
	cran = "jadeLizardOptions" 

	version("1.0.1", md5="dfce6232ea3a15b162dfdd3bb3ea5fda")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
