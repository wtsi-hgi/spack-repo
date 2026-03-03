# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFuzzystattraeoo(RPackage):
	"""Package 'FuzzyStatTra' in Encapsulated Object Oriented
Programming

	The aim of the package is to contain the package 'FuzzyStatTra' in 
    Encapsulated Object Oriented Programming using R6. 'FuzzyStatTra' contains Statistical 
    Methods for Trapezoidal Fuzzy Numbers, whose aim is to provide some basic functions 
    for doing statistical analysis with trapezoidal fuzzy numbers. For more details, you 
    can visit the website of the SMIRE+CoDiRE (Statistical Methods with Imprecise Random 
    Elements and Comparison of Distributions of Random Elements) Research Group 
    (<https://bellman.ciencias.uniovi.es/smire+codire/>). The most related paper can be 
    found in References. Now, those functions are organized in specific classes and methods. 
    This object-based approach is an important step in making statistical computing more 
    accessible to users.
	"""
	
	homepage = "https://bellman.ciencias.uniovi.es/smire+codire/FuzzyStatTraRpackage.html"
	cran = "FuzzyStatTraEOO" 

	version("1.0", md5="05f9e4c23026d8906f7bae37225c28d4")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
