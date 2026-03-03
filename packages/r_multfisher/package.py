# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultfisher(RPackage):
	"""Optimal Exact Tests for Multiple Binary Endpoints

	Calculates exact hypothesis tests to compare a treatment and a reference group with respect to multiple binary endpoints.
    The tested null hypothesis is an identical multidimensional distribution of successes and failures in both groups. The alternative
    hypothesis is a larger success proportion in the treatment group in at least one endpoint. The tests are based on the multivariate
    permutation distribution of subjects between the two groups. For this permutation distribution, rejection regions are calculated 
    that satisfy one of different possible optimization criteria. In particular, regions with maximal exhaustion of the nominal
    significance level, maximal power under a specified alternative or maximal number of elements can be found. Optimization is achieved
    by a branch-and-bound algorithm. By application of the closed testing principle, the global hypothesis tests are extended to multiple
    testing procedures.
	"""
	
	cran = "multfisher" 

	version("1.1", md5="f34db0c27e193cc8cd043f6a97beaf78")

	depends_on("r@3:", type=("build", "run"))
