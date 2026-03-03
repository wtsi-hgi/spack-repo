# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesdip(RPackage):
	"""Bayesian Decreasingly Informative Priors for Early Termination
Phase II Trials

	Provide early termination phase II trial designs with a
    decreasingly informative prior (DIP) or a regular Bayesian prior
    chosen by the user. The program can determine the minimum planned
    sample size necessary to achieve the user-specified admissible
    designs. The program can also perform power and expected sample size
    calculations for the tests in early termination Phase II trials.
    See Wang C and Sabo RT (2022) <doi:10.18203/2349-3259.ijct20221110>;
    Sabo RT (2014) <doi:10.1080/10543406.2014.888441>.
	"""
	
	homepage = "<https://github.com/chenw10/BayesDIP>"
	cran = "BayesDIP" 

	version("0.1.1", md5="6659ac9f1d35979b96380dd0103e653f")

