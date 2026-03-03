# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRankdifferencetest(RPackage):
	"""Kornbrot's Rank Difference Test

	Implements Kornbrot's rank difference test as described in 
    <doi:10.1111/j.2044-8317.1990.tb00939.x>. This method is a modified 
    Wilcoxon signed-rank test which produces consistent and meaningful 
    results for ordinal or monotonically-transformed data.
	"""
	
	homepage = "http://brettklamer.com/work/rankdifferencetest"
	cran = "rankdifferencetest" 

	version("2021-11-25", md5="9b9876279179035bd622ae86d359c47e")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-coin", type=("build", "run"))
	depends_on("r-modeltools", type=("build", "run"))
