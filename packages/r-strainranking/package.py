# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStrainranking(RPackage):
	"""Ranking of Pathogen Strains

	Regression-based ranking of pathogen strains with respect to their contributions to natural epidemics, using demographic and genetic data sampled in the curse of the epidemics. This package also includes the GMCPIC test.
	"""
	
	cran = "StrainRanking" 

	version("1.2", md5="d2eb9a5d7b69adbea6958b51dc4d264a")

	depends_on("r@3:", type=("build", "run"))
