# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBcrm(RPackage):
	"""Bayesian Continual Reassessment Method for Phase I
Dose-Escalation Trials

	Implements a wide variety of one- and two-parameter Bayesian CRM
    designs. The program can run interactively, allowing the user to enter outcomes
    after each cohort has been recruited, or via simulation to assess operating
    characteristics. See Sweeting et al. (2013): <doi:10.18637/jss.v054.i13>.
	"""
	
	homepage = "https://github.com/mikesweeting/bcrm"
	cran = "bcrm" 

	version("0.5.4", md5="7a87f176c8ad8a9cb7f65f4a5c6cddd8")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggplot2@1.0.1:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
