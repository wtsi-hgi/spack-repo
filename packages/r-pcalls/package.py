# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcalls(RPackage):
	"""Pricing of Different Types of Call

	Compute the price of different types of call using different methods. The types available are Vanilla European Calls, Vanilla American Calls and American Digital Calls. Available methods are Montecarlo Simulation, Montecarlo Simulation with Antithetic Variates, Black-Scholes and the Binary Tree.  
	"""
	
	cran = "pcalls" 

	version("1.0", md5="58c440d220ed358ce68991ad7e310902")

	depends_on("r@3.5:", type=("build", "run"))
