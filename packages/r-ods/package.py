# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROds(RPackage):
	"""Statistical Methods for Outcome-Dependent Sampling Designs

	Outcome-dependent sampling (ODS) schemes are cost-effective ways to enhance study efficiency. 
    In ODS designs, one observes the exposure/covariates with a probability that depends on the outcome 
    variable. Popular ODS designs include case-control for binary outcome, case-cohort for time-to-event 
    outcome, and continuous outcome ODS design (Zhou et al. 2002) <doi: 10.1111/j.0006-341X.2002.00413.x>. 
    Because ODS data has biased sampling nature, standard statistical analysis such as linear regression 
    will lead to biases estimates of the population parameters. This package implements four statistical 
    methods related to ODS designs: (1) An empirical likelihood method analyzing the primary continuous 
    outcome with respect to exposure variables in continuous ODS design (Zhou et al., 2002). (2) A partial 
    linear model analyzing the primary outcome in continuous ODS design (Zhou, Qin and Longnecker, 2011) 
    <doi: 10.1111/j.1541-0420.2010.01500.x>. (3) Analyze a secondary outcome in continuous ODS design 
    (Pan et al. 2018) <doi: 10.1002/sim.7672>. (4) An estimated likelihood method analyzing a secondary 
    outcome in case-cohort data (Pan et al. 2017) <doi: 10.1111/biom.12838>.
	"""
	
	homepage = "https://github.com/Yinghao-Pan/ODS"
	cran = "ODS" 

	version("0.2.0", md5="499c8d30604e6c960ee8afa678e82fe4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cubature@1.4.1:", type=("build", "run"))
	depends_on("r-survival@2.42.3:", type=("build", "run"))
