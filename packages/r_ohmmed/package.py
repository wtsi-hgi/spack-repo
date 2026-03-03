# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROhmmed(RPackage):
	"""HMMs with Ordered Hidden States and Emission Densities

	Inference using a class of Hidden Markov models
    (HMMs) called 'oHMMed'(ordered HMM with emission densities 
    <doi:10.1101/2023.06.26.546495>): The 'oHMMed' algorithms identify 
    the number of comparably homogeneous regions within observed sequences
    with autocorrelation patterns. These are modelled as discrete hidden
    states; the observed data points are then realisations of continuous
    probability distributions with state-specific means that enable
    ordering of these distributions. The observed sequence is labelled
    according to the hidden states, permitting only neighbouring states
    that are also neighbours within the ordering of their associated
    distributions. The parameters that characterise these state-specific
    distributions are then inferred. Relevant for application to genomic
    sequences, time series, or any other sequence data with serial
    autocorrelation.
	"""
	
	homepage = "https://github.com/LynetteCaitlin/oHMMed"
	cran = "oHMMed" 

	version("1.0.1", md5="11bf335dd86659883a3488333f3d0a78")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cvms", type=("build", "run"))
	depends_on("r-ggmcmc", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-mistr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-vcd", type=("build", "run"))
