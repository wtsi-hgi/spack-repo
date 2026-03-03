# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCarbayesdata(RPackage):
	"""Data Used in the Vignettes Accompanying the CARBayes and
CARBayesST Packages

	Spatio-temporal data from Scotland used in the vignettes accompanying the CARBayes (spatial modelling) and CARBayesST (spatio-temporal modelling) packages. Most of the data relate to the set of 271 Intermediate Zones (IZ)  that make up the 2001 definition of the  Greater Glasgow and Clyde health board. 
	"""
	
	cran = "CARBayesdata" 

	version("3.0", md5="da717b37cb3efbcfa5525460ba37a8da")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
