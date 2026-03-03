# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPomic(RPackage):
	"""Pattern Oriented Modelling Information Criterion

	Calculations of an information criterion are proposed to check the quality of simulations results of Agent-based models (ABM/IBM) or other non-linear rule-based models. The POMDEV measure (Pattern Oriented Modelling DEViance) is based on the Kullback-Leibler divergence and likelihood theory. It basically indicates the deviance of simulation results from field observations. Once POMDEV scores and metropolis-hasting sampling on different model versions are effectuated, POMIC scores (Pattern Oriented Modelling Information Criterion) can be calculated. This method could be further developed to incorporate multiple patterns assessment. Piou C, U Berger and V Grimm (2009) <doi:10.1016/j.ecolmodel.2009.05.003>.
	"""
	
	cran = "Pomic" 

	version("1.0.4", md5="4ac8123c735c330b96feef0240b92bb1")

