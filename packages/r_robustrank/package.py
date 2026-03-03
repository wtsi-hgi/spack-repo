# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobustrank(RPackage):
	"""Robust Rank-Based Tests

	Implements two-sample tests for paired data with missing values (Fong, Huang, Lemos and McElrath 2018, Biostatics, <doi:10.1093/biostatistics/kxx039>) and modified Wilcoxon-Mann-Whitney two sample location test, also known as the Fligner-Policello test. 
	"""
	
	cran = "robustrank" 

	version("2024.1-28", md5="8474a666fc537c69c295bf6f6b8b7187")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-kyotil", type=("build", "run"))
