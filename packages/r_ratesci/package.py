# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRatesci(RPackage):
	"""Confidence Intervals for Comparisons of Binomial or Poisson
Rates

	Computes confidence intervals for the rate (or risk)
    difference ('RD') or rate ratio (or relative risk, 'RR') for 
    binomial proportions or Poisson rates, or for odds ratio 
    ('OR', binomial only). Also confidence intervals for a single 
    binomial or Poisson rate, and intervals for matched pairs. 
    Includes skewness-corrected asymptotic score ('SCAS') methods, 
    which have been developed in Laud (2017) <doi:10.1002/pst.1813>
    from Miettinen & Nurminen (1985) <doi:10.1002/sim.4780040211> and 
    Gart & Nam (1988) <doi:10.2307/2531848>. The same score produces 
    hypothesis tests analogous to the test for binomial RD and RR by 
    Farrington & Manning (1990) <doi:10.1002/sim.4780091208>. 
    The package also includes MOVER methods
    (Method Of Variance Estimates Recovery) for all contrasts, derived 
    from the Newcombe method but using equal-tailed Jeffreys intervals,
    and generalised for Bayesian applications incorporating prior 
    information. So-called 'exact' methods for strictly conservative 
    coverage are approximated using continuity corrections.
    Also includes methods for stratified calculations (e.g. meta-analysis),
    either assuming fixed effects (matching the CMH test) or incorporating 
    stratum heterogeneity.
	"""
	
	cran = "ratesci" 

	version("0.4-0", md5="1b0957e5bfb0ae785318e33489a1a49d")

	depends_on("r@3.6:", type=("build", "run"))
