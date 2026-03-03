# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RValottery(RPackage):
	"""Results from the Virginia Lottery Draw Games

	Historical results for the state of Virginia lottery draw games. Data were downloaded from https://www.valottery.com/. 
	"""
	
	cran = "valottery" 

	version("0.0.1", md5="41dcde66027cc4af384c408981a8475a")

