# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDixon(RPackage):
	"""Nearest Neighbour Contingency Table Analysis

	Function to test spatial segregation and association based in contingency table analysis of nearest neighbour counts following Dixon (2002) <doi:10.1080/11956860.2002.11682700>. Some 'Fortran' code has been included to the original dixon2002() function of the 'ecespa' package to improve speed.
	"""
	
	cran = "dixon" 

	version("0.0-9", md5="50cc84d4b92913346a5d1b4f1a840ceb")

	depends_on("r-splancs", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat@2.0.0:", type=("build", "run"))
