# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApproxmatch(RPackage):
	"""Approximately Optimal Fine Balance Matching with Multiple Groups

	Tools for constructing a matched design with multiple comparison groups.
 Further specifications of refined covariate balance restriction and exact match on 
 covariate can be imposed. Matches are approximately optimal in  the sense that the 
 cost of the solution is at most twice the optimal cost, Crama and Spieksma (1992) 
 <doi:10.1016/0377-2217(92)90078-N>, Karmakar, Small and Rosenbaum (2019)
 <doi:10.1080/10618600.2019.1584900>.
	"""
	
	cran = "approxmatch" 

	version("2.0", md5="07fd8ddb981c7929acc7adbc8bdf6402")

