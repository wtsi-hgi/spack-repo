# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLswplib(RPackage):
	"""Simulation and Spectral Estimation of Locally Stationary Wavelet
Packet Processes

	Library of functions for the statistical analysis and simulation of Locally Stationary Wavelet Packet (LSWP) processes.  The methods implemented by this library are described in Cardinali and Nason (2017) <doi:10.1111/jtsa.12230>.
	"""
	
	cran = "LSWPlib" 

	version("0.1.0", md5="25a7082715637cd310ff5604bc6f07cd")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-waveslim", type=("build", "run"))
	depends_on("r-wavethresh", type=("build", "run"))
