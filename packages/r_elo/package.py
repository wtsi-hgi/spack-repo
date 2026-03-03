# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElo(RPackage):
	"""Ranking Teams by Elo Rating and Comparable Methods

	A flexible framework for calculating Elo ratings and resulting
    rankings of any two-team-per-matchup system (chess, sports leagues, 'Go',
    etc.). This implementation is capable of evaluating a variety of matchups,
    Elo rating updates, and win probabilities, all based on the basic Elo
    rating system. It also includes methods to benchmark performance,
    including logistic regression and Markov chain models.
	"""
	
	homepage = "https://github.com/eheinzen/elo"
	cran = "elo" 

	version("3.0.2", md5="17b59b82c887efed8566b17e6cad1f89")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
