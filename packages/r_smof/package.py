# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmof(RPackage):
	"""Scoring Methodology for Ordered Factors

	Starting from a given object representing a fitted model (within
  a certain set of model classes) whose linear predictor includes some ordered 
  factor(s) among the explanatory variables, a new model is constructed and
  fitted where each named factor is replaced by a single numeric score, suitably
  chosen so that the new variable produces a fit comparable with the standard
  methodology based on a set of polynomial contrasts. Reference: Azzalini (2023) 
  <doi:10.1002/sta4.624>.
	"""
	
	cran = "smof" 

	version("1.1.0", md5="72ae44f4aebc33b52d5da0c31f06308a")
	version("1.0", md5="d97bca039b778ec651345fa0924658c3")

	depends_on("r@4:", type=("build", "run"))
