# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStratifiedbalancing(RPackage):
	"""Stratified Covariate Balancing

	Performs Stratified Covariate Balancing with Markov blanket feature selection and use of synthetic cases. See Alemi et al. (2016) <DOI:10.1111/1475-6773.12628>.
	"""
	
	cran = "StratifiedBalancing" 

	version("0.3.0", md5="64673dd5cc7c61404cf26b2cb857c3a7")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-bnlearn", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
