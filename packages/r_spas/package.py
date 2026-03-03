# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpas(RPackage):
	"""Stratified-Petersen Analysis System

	The Stratified-Petersen Analysis System (SPAS) is designed
    to estimate abundance in two-sample capture-recapture experiments 
    where the capture and recaptures are stratified. This is a generalization
    of the simple Lincoln-Petersen estimator.
    Strata may be defined in time or in space or both, 
    and the s strata in which marking takes place 
    may differ from the t strata in which recoveries take place.
    When s=t, SPAS reduces to the method described by 
    Darroch (1961) <doi:10.2307/2332748>.
    When s<t, SPAS implements the methods described in
    Plante, Rivest, and Tremblay (1988) <doi:10.2307/2533994>.
    Schwarz and Taylor (1998) <doi:10.1139/f97-238> describe
    the use of SPAS in estimating return of salmon stratified by
    time and geography. 
    A related package, BTSPAS, deals with temporal stratification where 
    a spline is used to model the distribution of the population 
    over time as it passes the second capture location.
    This is the R-version of the (now obsolete) standalone Windows 
    program available at <https://home.cs.umanitoba.ca/~popan/spas/spas_home.html>.
	"""
	
	cran = "SPAS" 

	version("2024.1.31", md5="69d189620f60b202a5176f2ab642baa7")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-tmb", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
