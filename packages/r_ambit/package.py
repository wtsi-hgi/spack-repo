# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmbit(RPackage):
	"""Simulation and Estimation of Ambit Processes

	Simulation and estimation tools for 
    various types of ambit processes, including trawl processes and weighted
    trawl processes. 
	"""
	
	cran = "ambit" 

	version("0.1.2", md5="bd41a190c697680caa676644a944b12b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-fbasics", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
