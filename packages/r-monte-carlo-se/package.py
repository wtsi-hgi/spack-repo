# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMonteCarloSe(RPackage):
	"""Monte Carlo Standard Errors

	Computes Monte Carlo standard errors for summaries of Monte Carlo output. Summaries and their standard errors are based on columns of Monte Carlo simulation output. Dennis D. Boos and Jason A. Osborne (2015) <doi:10.1111/insr.12087>.
	"""
	
	cran = "Monte.Carlo.se" 

	version("0.1.1", md5="25ab6721023e7af2ff6d692348ae2309")

