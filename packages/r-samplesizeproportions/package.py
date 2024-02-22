# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSamplesizeproportions(RPackage):
	"""Calculating Sample Size Requirements when Estimating the
Difference Between Two Binomial Proportions

	Sample size requirements calculation 
        using three different Bayesian criteria in the
        context of designing an experiment to estimate the difference
        between two binomial proportions. Functions for calculation of
        required sample sizes for the Average Length Criterion, the
        Average Coverage Criterion and the Worst Outcome Criterion in
        the context of binomial observations are provided. In all
        cases, estimation of the difference between two binomial
        proportions is considered. Functions for both the fully
        Bayesian and the mixed Bayesian/likelihood approaches are
        provided.
        For reference see Joseph L., du Berger R. and Bélisle P. (1997)
        <doi:10.1002/(sici)1097-0258(19970415)16:7%3C769::aid-sim495%3E3.0.co;2-v>.
	"""
	
	cran = "SampleSizeProportions" 

	version("1.1.3", md5="5db665e3c530318ae437aa2a1eb33ac3")

