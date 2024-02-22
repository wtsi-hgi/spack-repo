# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMinedfind(RPackage):
	"""A Bayesian Design for Minimum Effective Dosing-Finding Trial

	The nonparametric two-stage Bayesian adaptive design is a novel phase II clinical trial design for finding the minimum effective dose (MinED). This design is motivated by the top priority and concern of clinicians when testing a new drug, which is to effectively treat patients and minimize the chance of exposing them to subtherapeutic or overly toxic doses. It is used to design single-agent trials. 
	"""
	
	cran = "MinEDfind" 

	version("0.1.3", md5="a8d585ba2e529b6ff0f3221558ebac42")

	depends_on("r-iso", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
