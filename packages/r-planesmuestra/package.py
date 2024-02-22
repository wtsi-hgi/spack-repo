# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlanesmuestra(RPackage):
	"""Functions for Calculating Dodge Romig, MIL STD 105E and MIL STD
414 Acceptance Sampling Plan

	Calculates an acceptance sampling plan, (sample size and acceptance number) based in MIL STD 105E, Dodge  Romig and MIL STD 414 tables and procedures. The arguments for each function are related to lot size, inspection level and quality level. The specific plan operating curve (OC), is calculated by the binomial distribution.  
	"""
	
	cran = "Planesmuestra" 

	version("0.1", md5="3b20a09d8592e203bd2eff5b43b06807")

