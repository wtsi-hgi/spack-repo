# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovidprobability(RPackage):
	"""Estimate the Unit-Wide Probability of COVID-19

	We propose a method to estimate the probability of an 
    undetected case of COVID-19 in a defined setting, when a given number of 
    people have been exposed, with a given pretest probability of having 
    COVID-19 as a result of that exposure. Since we are interested in undetected
    COVID-19, we assume no person has developed symptoms (which would warrant 
    further investigation) and that everyone was tested on a given day, and all 
    tested negative.
	"""
	
	homepage = "https://github.com/eebrown/covidprobability"
	cran = "covidprobability" 

	version("0.1.0", md5="b966e4111eb79259bf0c61cf6381b4fb")

	depends_on("r@2.10:", type=("build", "run"))
