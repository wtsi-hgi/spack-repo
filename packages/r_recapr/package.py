# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRecapr(RPackage):
	"""Two Event Mark-Recapture Experiment

	Tools are provided for estimating, testing, and simulating
    abundance in a two-event (Petersen) mark-recapture experiment. Functions are
    given to calculate the Petersen, Chapman, and Bailey estimators and associated
    variances. However, the principal utility is a set of functions to simulate
    random draws from these estimators, and use these to conduct hypothesis
    tests and power calculations. Additionally, a set of functions are provided
    for generating confidence intervals via bootstrapping. Functions are also
    provided to test abundance estimator consistency under complete or partial
    stratification, and to calculate stratified or partially stratified estimators.
    Functions are also provided to calculate recommended sample sizes.
    Referenced methods can be found in Arnason et al. (1996) <ISSN:0706-6457>, 
    Bailey (1951) <DOI:10.2307/2332575>, 
    Bailey (1952) <DOI:10.2307/1913>, 
    Chapman (1951) NAID:20001644490, 
    Cohen (1988) ISBN:0-12-179060-6, 
    Darroch (1961) <DOI:10.2307/2332748>, and
    Robson and Regier (1964) <ISSN:1548-8659>.
	"""
	
	cran = "recapr" 

	version("0.4.4", md5="2fde74b7296247c2282f51734aeb402a")

	depends_on("r-mass", type=("build", "run"))
