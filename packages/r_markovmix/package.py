# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarkovmix(RPackage):
	"""Mixture of Markov Chains with Support of Higher Orders and
Multiple Sequences

	Fit mixture of Markov chains of higher orders from multiple
    sequences. It is also compatible with ordinary 1-component, 1-order or
    single-sequence Markov chains. Various utility functions are provided
    to derive transition patterns, transition probabilities per component
    and component priors. In addition, print(), predict() and component
    extracting/replacing methods are also defined as a convention of
    mixture models.
	"""
	
	homepage = "https://github.com/zhuxr11/markovmix"
	cran = "markovmix" 

	version("0.1.3", md5="0b835498261beb976cc2db7b322d3924")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@1.0.8:", type=("build", "run"))
	depends_on("r-forcats@1:", type=("build", "run"))
	depends_on("r-pillar@1.9:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-tibble@3.1.6:", type=("build", "run"))
	depends_on("r-tidyr@1.2:", type=("build", "run"))
