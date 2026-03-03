# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKendallrandomwalks(RPackage):
	"""Simulate and Visualize Kendall Random Walks and Related
Distributions

	Kendall random walks are a continuous-space Markov chains generated
             by the Kendall generalized convolution. This package provides tools
             for simulating these random walks and studying distributions
             related to them. For more information about Kendall random walks see Jasiulis-Gołdyn (2014) <arXiv:1412.0220>.
	"""
	
	cran = "kendallRandomWalks" 

	version("0.9.4", md5="9b9bd38eb3ccde259d4b199ce8db88d4")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-actuar", type=("build", "run"))
