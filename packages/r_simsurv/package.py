# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimsurv(RPackage):
	"""Simulate Survival Data

	Simulate survival times from standard parametric survival
    distributions (exponential, Weibull, Gompertz), 2-component mixture
    distributions, or a user-defined hazard, log hazard, cumulative hazard,
    or log cumulative hazard function. Baseline covariates can be included
    under a proportional hazards assumption.
    Time dependent effects (i.e. non-proportional hazards) can be included by
    interacting covariates with linear time or a user-defined function of time.
    Clustered event times are also accommodated.
    The 2-component mixture distributions can allow for a variety of flexible
    baseline hazard functions reflecting those seen in practice.
    If the user wishes to provide a user-defined
    hazard or log hazard function then this is possible, and the resulting
    cumulative hazard function does not need to have a closed-form solution.
    For details see the supporting paper <doi:10.18637/jss.v097.i03>.
    Note that this package is modelled on the 'survsim' package available in
    the 'Stata' software (see Crowther and Lambert (2012)
    <https://www.stata-journal.com/sjpdf.html?articlenum=st0275> or
    Crowther and Lambert (2013) <doi:10.1002/sim.5823>).
	"""
	
	cran = "simsurv" 

	version("1.0.0", md5="ad848b1f06d71cbdea8512f81391a2e1")

	depends_on("r@3.3:", type=("build", "run"))
