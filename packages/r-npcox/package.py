# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNpcox(RPackage):
	"""Nonparametric and Semiparametric Proportional Hazards Model

	An estimation procedure for the analysis of nonparametric proportional hazards model (e.g. h(t) = h0(t)exp(b(t)'Z)), providing estimation of b(t) and its pointwise standard errors, and semiparametric proportional hazards model (e.g. h(t) = h0(t)exp(b(t)'Z1 + c*Z2)), providing estimation of b(t), c and their standard errors. More details can be found in Lu Tian et al. (2005) <doi:10.1198/016214504000000845>.
	"""
	
	cran = "NPCox" 

	version("1.2", md5="281e96c842d7d158e6540c4b5b67eb63")

