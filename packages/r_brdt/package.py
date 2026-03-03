# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrdt(RPackage):
	"""Binomial Reliability Demonstration Tests

	This is an implementation of design methods for binomial reliability demonstration tests (BRDTs) with failure count data. 
    The acceptance decision uncertainty of BRDT has been quantified and the impacts of the uncertainty on related reliability assurance activities such as reliability growth (RG) and warranty services (WS) are evaluated.
    This package is associated with the work from the published paper "Optimal Binomial Reliability Demonstration Tests Design under Acceptance Decision Uncertainty" by Suiyao Chen et al. (2020) <doi:10.1080/08982112.2020.1757703>.
	"""
	
	homepage = "https://github.com/ericchen12377/BRDT"
	cran = "BRDT" 

	version("0.1.0", md5="ef08747440811693d33ab9b32bf9febf")

	depends_on("r@3.3:", type=("build", "run"))
