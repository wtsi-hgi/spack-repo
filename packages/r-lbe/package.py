# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLbe(RPackage):
	"""Estimation of the false discovery rate.

	LBE is an efficient procedure for estimating the proportion of true null hypotheses, the false discovery rate (and so the q-values) in the framework of estimating procedures based on the marginal distribution of the p-values without assumption for the alternative hypothesis.
	"""
	
	bioc = "LBE"

	version("1.76.0", commit="8c748257219c6eccd974e034a6d892d8e325b2a5")
	version("1.70.0", commit="e846862e6cc922deba089a84ffb59603adc52b22")

