# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBoin(RPackage):
	"""Bayesian Optimal INterval (BOIN) Design for Single-Agent and
Drug- Combination Phase I Clinical Trials

	The Bayesian optimal interval (BOIN) design is a novel phase I
    clinical trial design for finding the maximum tolerated dose (MTD). It can be
    used to design both single-agent and drug-combination trials. The BOIN design
    is motivated by the top priority and concern of clinicians when testing a new
    drug, which is to effectively treat patients and minimize the chance of exposing
    them to subtherapeutic or overly toxic doses. The prominent advantage of the
    BOIN design is that it achieves simplicity and superior performance at the same
    time. The BOIN design is algorithm-based and can be implemented in a simple
    way similar to the traditional 3+3 design. The BOIN design yields an average
    performance that is comparable to that of the continual reassessment method
    (CRM, one of the best model-based designs) in terms of selecting the MTD, but
    has a substantially lower risk of assigning patients to subtherapeutic or overly
    toxic doses. For tutorial, please check Yan et al. (2020) <doi:10.18637/jss.v094.i13>.
	"""
	
	cran = "BOIN" 

	version("2.7.2", md5="3988eb19f69d6d3854dfb7ae86974903")

	depends_on("r-iso", type=("build", "run"))
