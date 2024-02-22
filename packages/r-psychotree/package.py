# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsychotree(RPackage):
	"""Recursive Partitioning Based on Psychometric Models

	Recursive partitioning based on psychometric models,
  employing the general MOB algorithm (from package partykit) to obtain
  Bradley-Terry trees, Rasch trees, rating scale and partial credit trees, and
  MPT trees, trees for 1PL, 2PL, 3PL and 4PL models and generalized partial 
  credit models.
	"""
	
	cran = "psychotree" 

	version("0.16-0", md5="baf39b9fe030fad8886ae6804e73da6b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-partykit@1.2.9:", type=("build", "run"))
	depends_on("r-psychotools@0.7.1:", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
