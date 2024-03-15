# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMortaar(RPackage):
	"""Analysis of Archaeological Mortality Data

	A collection of functions for the analysis of archaeological mortality
    data (on the topic see e.g. Chamberlain 2006 
    <https://books.google.de/books?id=nG5FoO_becAC&lpg=PA27&ots=LG0b_xrx6O&dq=life%20table%20archaeology&pg=PA27#v=onepage&q&f=false>). 
    It takes demographic data in different formats and displays the result in a standard life table
    as well as plots the relevant indices (percentage of deaths, survivorship, probability of death, life expectancy, percentage of population).
	"""
	
	homepage = "https://github.com/ISAAKiel/mortAAR"
	cran = "mortAAR" 

	version("1.1.6", md5="a503244f5181a3e7a3517cf0e6d88c1f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-rdpack@0.4.20:", type=("build", "run"))
	depends_on("r-reshape2@1.4.2:", type=("build", "run"))
	depends_on("r-tibble@3.0.3:", type=("build", "run"))
	depends_on("r-rlang@1.1.1:", type=("build", "run"))
