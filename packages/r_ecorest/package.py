# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcorest(RPackage):
	"""Conducts Analyses Informing Ecosystem Restoration Decisions

	Three sets of data and functions for informing ecosystem restoration
    decisions, particularly in the context of the U.S. Army Corps of Engineers.
    First, model parameters are compiled as a data set and associated metadata 
    for over 500 habitat suitability models developed by the U.S. Fish and 
    Wildlife Service (USFWS 1980) <https://www.fws.gov/policy/ESMindex.html>. 
    Second, functions for conducting habitat suitability analyses both for the
    models described above as well as generic user-specified model 
    parameterizations. Third, a suite of decision support tools for conducting 
    cost-effectiveness and incremental cost analyses (Robinson et al. 1995)
    <https://www.iwr.usace.army.mil/Portals/70/docs/iwrreports/95-R-1.pdf>.
	"""
	
	cran = "ecorest" 

	version("1.0.0", md5="f7a77b6af25fdf6be1a2f3baee38049b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
