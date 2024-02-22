# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlfm(RPackage):
	"""Probabilistic Latent Feature Analysis

	Functions for estimating probabilistic latent feature models with a disjunctive, conjunctive or additive mapping rule on (aggregated) binary three-way data.
	"""
	
	cran = "plfm" 

	version("2.2.6", md5="8d85bf572856699dd1d727e40ea85392")

	depends_on("r-sfsmisc", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
