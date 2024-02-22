# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTlaginterim(RPackage):
	"""Interim Monitoring of Clinical Trials with Time-Lagged Outcome

	Implements inverse and augmented inverse probability weighted 
    estimators for common treatment effect parameters at an interim analysis 
    with time-lagged outcome that may not be available for all enrolled subjects.  
    Produces estimators, standard errors, and information that can be used to 
    compute stopping boundaries using software that assumes that the 
    estimators/test statistics have independent increments. 
    Tsiatis, A. A. and Davidian, M., (2022) <arXiv:2204.10739> .
	"""
	
	cran = "tLagInterim" 

	version("1.0", md5="57f5218a7a4418993b571ca281bc9415")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
