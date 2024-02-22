# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RValueeq5d(RPackage):
	"""Scoring EQ-5d Descriptive System

	EQ-5D is a standard instrument (<https://euroqol.org/eq-5d-instruments/>) that measures the quality of life 
    often used in clinical and economic evaluations of health care technologies. Both adult versions of EQ-5D (EQ-5D-3L and EQ-5D-5L)
    contain a descriptive system and visual analog scale. The descriptive system measures the patient's health in 5 dimensions: 
    the 5L versions has 5 levels and 3L version has 3 levels. The descriptive system scores are usually converted to index values 
    using country specific values sets (that incorporates the country preferences). This package allows the calculation of both descriptive system
    scores to the index value scores. The value sets for EQ-5D-3L are from the references mentioned in the website <https://euroqol.org/eq-5d-instruments/eq-5d-3l-about/valuation/>
    The value sets for EQ-5D-3L for a total of 31 countries are used for the valuation (see the user guide for a complete list of references).
    The value sets for EQ-5D-5L are obtained from references mentioned in the <https://euroqol.org/eq-5d-instruments/eq-5d-5l-about/valuation-standard-value-sets/> and other sources.
    The value sets for EQ-5D-5L for a total of 17 countries are used for the valuation (see the user guide for a complete list of references).
    The package can also be used to map 5L scores to 3L index values for 10 countries: Denmark, France, Germany, Japan, Netherlands, Spain, Thailand, UK, USA, and Zimbabwe. 
    The value set and method for mapping are obtained from Van Hout et al (2012) <doi: 10.1016/j.jval.2012.02.008>. 
	"""
	
	cran = "valueEQ5D" 

	version("0.7.2", md5="bf241b27a4a1c150244055e74af9a1ab")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
