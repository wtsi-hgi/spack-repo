# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2beat(RPackage):
	"""Multistage Sampling Allocation and Sample Selection

	Multivariate optimal allocation for different domains in one and two stages stratified sample design. 'R2BEAT' extends the Neyman (1934) – Tschuprow (1923) allocation method to the case of several variables, adopting a generalization of the Bethel’s proposal (1989). 'R2BEAT' develops this methodology but, moreover, it allows to determine the sample allocation in the multivariate and multi-domains case of estimates for two-stage stratified samples. It also allows to perform both Primary Stage Units and Secondary Stage Units selection. This package requires the availability of 'ReGenesees', that can be installed from <https://github.com/DiegoZardetto/ReGenesees>.
	"""
	
	homepage = "https://barcaroli.github.io/R2BEAT/"
	cran = "R2BEAT" 

	version("1.0.5", md5="94c8b8df85851540b50dadc77a8d2e2a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sampling", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
