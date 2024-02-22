# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvidencesynthesis(RPackage):
	"""Synthesizing Causal Evidence in a Distributed Research Network

	Routines for combining causal effect estimates and study diagnostics across multiple data sites in a distributed study, without sharing patient-level data. 
  Allows for normal and non-normal approximations of the data-site likelihood of the effect parameter. 
	"""
	
	homepage = "https://ohdsi.github.io/EvidenceSynthesis/"
	cran = "EvidenceSynthesis" 

	version("0.5.0", md5="50f2d18bf5780b3ae2ee3f32f08c958a")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggdist", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-meta", type=("build", "run"))
	depends_on("r-empiricalcalibration", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-beastjar", type=("build", "run"))
	depends_on("r-cyclops@3.1:", type=("build", "run"))
	depends_on("r-hdinterval", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("openjdk@8:", type=("build", "link", "run"))
