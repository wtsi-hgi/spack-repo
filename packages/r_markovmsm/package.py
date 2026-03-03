# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarkovmsm(RPackage):
	"""Methods for Checking the Markov Condition in Multi-State
Survival Data

	The inference in multi-state models is traditionally performed under
             a Markov assumption that claims that past and future of the process
             are independent given the present state. In this package, we 
             consider tests of the Markov assumption that are applicable to 
             general multi-state models. Three approaches using existing 
             methodology are considered: a simple method based on including
             covariates depending on the history in Cox models for the transition
             intensities; methods based on measuring the discrepancy of the 
             non-Markov estimators of the transition probabilities to the 
             Markov Aalen-Johansen estimators; and, finally, methods that were
             developed by considering summaries from families of log-rank 
             statistics where patients are grouped by the state occupied of the
             process at a particular time point (see Soutinho G, Meira-Machado L
             (2021) <doi:10.1007/s00180-021-01139-7> and Titman AC, Putter H
             (2020) <doi:10.1093/biostatistics/kxaa030>).
	"""
	
	cran = "markovMSM" 

	version("0.1.3", md5="94d084ba29d1bec10e2f35ad21e0f458")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mstate", type=("build", "run"))
