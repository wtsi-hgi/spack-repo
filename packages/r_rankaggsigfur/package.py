# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRankaggsigfur(RPackage):
	"""Polynomially Bounded Rank Aggregation under Kemeny's Axiomatic
Approach

	Polynomially bounded algorithms to aggregate complete rankings under Kemeny's axiomatic framework. 'RankAggSIgFUR' (pronounced as rank-agg-cipher) contains two heuristics algorithms: FUR and SIgFUR. For details, please see Badal and Das (2018) <doi:10.1016/j.cor.2018.06.007>.
	"""
	
	homepage = "https://github.com/prakashvs613/RankAggSIgFUR"
	cran = "RankAggSIgFUR" 

	version("1.0.0", md5="ee3f0381b120daac77b852c699ddc25b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
