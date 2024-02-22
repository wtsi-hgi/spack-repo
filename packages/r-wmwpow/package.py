# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWmwpow(RPackage):
	"""Precise and Accurate Power of the Wilcoxon-Mann-Whitney Rank-Sum
Test for a Continuous Variable

	Power calculator for the two-sample Wilcoxon-Mann-Whitney rank-sum test for a continuous outcome (Mollan, Trumble, Reifeis et. al., Mar. 2020) <doi:10.1080/10543406.2020.1730866> <arXiv:1901.04597>, (Mann and Whitney 1947) <doi:10.1214/aoms/1177730491>, (Shieh, Jan, and Randles 2006) <doi:10.1080/10485250500473099>.
	"""
	
	cran = "wmwpow" 

	version("0.1.3", md5="323281b9969994cf1c2823fe47da577b")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-lamw", type=("build", "run"))
	depends_on("r-smoothmest", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
