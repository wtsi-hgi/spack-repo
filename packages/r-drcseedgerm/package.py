# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrcseedgerm(RPackage):
	"""Utilities for Data Analyses in Seed Germination/Emergence Assays

	Utility functions to be used to analyse datasets obtained from seed germination/emergence assays. Fits several types of seed germination/emergence models, including those reported in Onofri et al. (2018) "Hydrothermal-time-to-event models for seed germination", European Journal of Agronomy, 101, 129-139 <doi:10.1016/j.eja.2018.08.011>. Contains several datasets for practicing. 
	"""
	
	homepage = "https://www.statforbiology.com"
	cran = "drcSeedGerm" 

	version("1.0.1", md5="678c08f6d495bf31ece27cea6388e9a8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-drc", type=("build", "run"))
	depends_on("r-drcte", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
