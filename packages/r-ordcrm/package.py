# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrdcrm(RPackage):
	"""Likelihood-Based Continual Reassessment Method (CRM) Dose
Finding Designs

	Provides the setup and calculations needed
        to run a likelihood-based continual reassessment method (CRM)
        dose finding trial and performs simulations to assess design
        performance under various scenarios. 3 dose finding designs
        are included in this package: ordinal proportional odds model
        (POM) CRM, ordinal continuation ratio (CR) model CRM, and the
        binary 2-parameter logistic model CRM.
        These functions allow customization of design characteristics
        to vary sample size, cohort sizes, target dose-limiting
        toxicity (DLT) rates, discrete or continuous dose levels,
        combining ordinal grades 0 and 1 into one category, and
        incorporate safety and/or stopping rules.
        For POM and CR model designs, ordinal toxicity grades are
        specified by common terminology criteria for adverse events
        (CTCAE) version 4.0.
        Function 'pseudodata' creates the necessary starting models
        for these 3 designs, and function 'nextdose' estimates the
        next dose to test in a cohort of patients for a target DLT
        rate.
        We also provide the function 'crmsimulations' to assess the
        performance of these 3 dose finding designs under various
        scenarios.
	"""
	
	cran = "ordcrm" 

	version("1.0.0", md5="40ff4b36c7530524ddff5e2ce8b01e22")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
