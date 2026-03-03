# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHoldem(RPackage):
	"""Texas Holdem Simulator

	Simulates hands and tournaments of Texas Holdem, 
	the most popular form of poker.
	For examples of probability problems involving Texas Holdem 
	and a brief explanation of the game see Schoenberg, F. (2011).
	An Introduction to Probability with Texas Hold'em Examples.
	Taylor and Francis, New York, ISBN-13: 978-1439827680. 
	"""
	
	cran = "holdem" 

	version("1.2", md5="25c4169792ddb7cf043429b06eb67af3")

