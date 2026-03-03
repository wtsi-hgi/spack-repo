# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpcwk(RPackage):
	"""Kendall's Tau Partial Corr. for Survival Trait and Biomarkers

	We propose the inverse probability-of-censoring weighted (IPCW) Kendall's tau to measure the association of the survival trait with biomarkers and Kendall's partial correlation to reflect the relationship of the survival trait with interaction variable conditional on main effects, as described in Wang and Chen (2020) <doi:10.1093/bioinformatics/btaa017>. 
	"""
	
	cran = "IPCWK" 

	version("1.0", md5="ac98e60c391bef03ad9d9358891fcbc8")

	depends_on("r@3.4.3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
