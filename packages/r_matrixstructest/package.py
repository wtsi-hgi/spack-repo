# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatrixstructest(RPackage):
	"""Tests of Matrix Structure for Construct Validation

	Tests for block-diagonal structure in symmetric matrices (e.g. correlation matrices) under the null hypothesis of exchangeable off-diagonal elements. As described in Segal et al. (2019), these tests can be useful for construct validation either by themselves or as a complement to confirmatory factor analysis. Monte Carlo methods are used to approximate the permutation p-value with Hubert's Gamma (Hubert, 1976) and a t-statistic. This package also implements the chi-squared statistic described by Steiger (1980). Please see Segal, et al. (2019) <doi:10.1007/s11336-018-9647-4> for more information.
	"""
	
	homepage = "https://github.com/bdsegal/matrixStrucTest"
	cran = "matrixStrucTest" 

	version("1.0.0", md5="4708a598a1144d52c28bc19dcaa30108")

	depends_on("r@3.1:", type=("build", "run"))
