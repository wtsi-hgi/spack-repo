# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgendata(RPackage):
	"""Generates Multivariate Nonnormal Data and Determines How Many
Factors to Retain

	The GenDataSample() and GenDataPopulation() functions create, 
    respectively, a sample or population of multivariate nonnormal data 
    using methods described in Ruscio and Kaczetow (2008). Both of these 
    functions call a FactorAnalysis() function to reproduce a correlation 
    matrix. The EFACompData() function allows users to determine how many 
    factors to retain in an exploratory factor analysis of an empirical data
    set using a method described in Ruscio and Roche (2012). The latter 
    function uses populations of comparison data created by calling the 
    GenDataPopulation() function.
    <DOI: 10.1080/00273170802285693>.
    <DOI: 10.1037/a0025697>.
	"""
	
	cran = "RGenData" 

	version("1.0", md5="eb116f8a004b1aa07352833fa894c3d8")

