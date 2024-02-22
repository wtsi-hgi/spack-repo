# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUdderquarterinfectiondata(RPackage):
	"""Udder Quarter Infection Data

	The udder quarter infection data set contains infection times of individual cow udder quarters with Corynebacterium bovis (Laevens et al. 1997 <DOI:10.3168/jds.S0022-0302(97)76295-7>). Obviously, the four udder quarters are clustered within a cow, and udder quarters are sampled only approximately monthly, generating interval-censored data. The data set contains both covariates that change within a cow (e.g., front and rear udder quarters) and covariates that change between cows (e.g., parity [the number of previous calvings]). The correlation between udder infection times within a cow also is of interest, because this is a measure of the infectivity of the agent causing the disease. Various models have been applied to address the problem of interdependence for right-censored event times. These models, as applied to this data set, can be found back in the publications found in the reference list.
	"""
	
	cran = "UdderQuarterInfectionData" 

	version("1.0.0", md5="56fe2a028e9c4ca414411621e40ae659")

