# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVistributions(RPackage):
	"""Visualize Probability Distributions

	Visualize and compute percentiles/probabilities of normal, t, f, chi square 
    and binomial distributions.
	"""
	
	homepage = "https://github.com/rsquaredacademy/vistributions"
	cran = "vistributions" 

	version("0.1.2", md5="853cf69d0308e4daf5f5e15b1855f340")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
