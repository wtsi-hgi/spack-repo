# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RToxcrit(RPackage):
	"""Calculates Safety Stopping Boundaries for a Single-Arm Trial
using Bayes

	Computation of stopping boundaries for a single-arm trial using a
    Bayesian criterion; i.e., for each m<=n (n= total patient number of the 
    trial) the smallest number of observed toxicities is calculated
    leading to the termination of the trial/accrual according to the specified 
    criteria. The probabilities of stopping the trial/accrual at and up until 
    (resp.) the m-th patient (m<=n) is also calculated. This design is more 
    conservative than the frequentist approach (using Clopper Pearson CIs)
    which might be preferred as it concerns safety.See also Aamot et.al.(2010) 
    "Continuous monitoring of toxicity in clinical trials - simulating the risk 
    of stopping prematurely" <doi:10.5414/cpp48476>.
	"""
	
	cran = "ToxCrit" 

	version("1.0", md5="debd6fb8416030063deaf457e2e2be77")

