# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHopbyhop(RPackage):
	"""Transmissions and Receptions in a Hop by Hop Network

	Computes the expectation of the number of transmissions and receptions considering a Hop-by-Hop transport model with limited number of retransmissions per packet. It provides the theoretical results shown in Palma et. al.(2016) <DOI:10.1109/TLA.2016.7555237> and also estimated values based on Monte Carlo simulations. It is also possible to consider random data and ACK probabilities.
	"""
	
	cran = "hopbyhop" 

	version("3.41", md5="33521dde917c3ba3838bbd27ff1c34d9")

	depends_on("r-pastecs", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
