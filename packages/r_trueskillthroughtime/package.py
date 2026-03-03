# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrueskillthroughtime(RPackage):
	"""Skill Estimation Based on a Single Bayesian Network

	
    Most estimators implemented by the video game industry cannot obtain reliable initial estimates nor guarantee comparability between distant estimates. TrueSkill Through Time solves all these problems by modeling the entire history of activities using a single Bayesian network allowing the information to propagate correctly throughout the system. This algorithm requires only a few iterations to converge, allowing millions of observations to be analyzed using any low-end computer.
    The core ideas implemented in this project were developed by Dangauthier P, Herbrich R, Minka T, Graepel T (2007). "Trueskill through time: Revisiting the history of chess." <https://dl.acm.org/doi/10.5555/2981562.2981605>.
	"""
	
	homepage = "https://github.com/glandfried/TrueSkillThroughTime.R"
	cran = "TrueSkillThroughTime" 

	version("0.1.1", md5="5bf5f6045a598d3f3bfee9b664060411")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-hash", type=("build", "run"))
