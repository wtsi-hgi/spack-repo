# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComperank(RPackage):
	"""Ranking Methods for Competition Results

	Compute ranking and rating based on competition
    results. Methods of different nature are implemented: with fixed
    Head-to-Head structure, with variable Head-to-Head structure and with
    iterative nature. All algorithms are taken from the book 'Who’s #1?:
    The science of rating and ranking' by Amy N. Langville and Carl D.
    Meyer (2012, ISBN:978-0-691-15422-0).
	"""
	
	homepage = "https://github.com/echasnovski/comperank"
	cran = "comperank" 

	version("0.1.1", md5="157f15ae8741f89e77393ab0418adc8c")

	depends_on("r-comperes@0.1:", type=("build", "run"))
	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr@0.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang@0.2:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
