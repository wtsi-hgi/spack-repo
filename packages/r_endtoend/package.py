# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REndtoend(RPackage):
	"""Transmissions and Receptions in an End to End Network

	Computes the expectation of the number of transmissions and receptions considering an End-to-End transport model with limited number of retransmissions per packet. It provides theoretical results and also estimated values based on Monte Carlo simulations. It is also possible to consider random data and ACK probabilities.
	"""
	
	cran = "endtoend" 

	version("2.29", md5="64b657f38a3788004dd080b2abc0e921")

	depends_on("r-pastecs", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
