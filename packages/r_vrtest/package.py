# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVrtest(RPackage):
	"""Variance Ratio Tests and Other Tests for Martingale Difference
Hypothesis

	A  collection of statistical tests for martingale difference hypothesis, including automatic portmanteau test (Escansiano and Lobato, 2009) <doi:10.1016/j.jeconom.2009.03.001> and automatic variance ratio test (Kim, 2009) <doi:10.1016/j.frl.2009.04.003>.
	"""
	
	cran = "vrtest" 

	version("1.2", md5="30fee9c9c9b68522bece16d0b123047d")

