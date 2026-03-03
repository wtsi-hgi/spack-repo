# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmac(RPackage):
	"""Genomic Mediation Analysis with Adaptive Confounding Adjustment

	Performs genomic mediation
    analysis with adaptive confounding adjustment (GMAC) proposed by Yang et al. (2017) <doi:10.1101/078683>. It implements large scale
    mediation analysis and adaptively selects potential confounding variables to
    adjust for each mediation test from a pool of candidate confounders. The package
    is tailored for but not limited to genomic mediation analysis (e.g., cis-gene
    mediating trans-gene regulation pattern where an eQTL, its cis-linking gene
    transcript, and its trans-gene transcript play the roles as treatment, mediator
    and the outcome, respectively), restricting to scenarios with the presence of
    cis-association (i.e., treatment-mediator association) and random eQTL (i.e.,
    treatment).
	"""
	
	cran = "GMAC" 

	version("3.1", md5="bc17d531ff898b97279d913064570f3f")

