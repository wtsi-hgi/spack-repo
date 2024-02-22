# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimjoint(RPackage):
	"""Simulate Joint Distribution

	Simulate multivariate correlated data given nonparametric marginals and their joint structure characterized by a Pearson or Spearman correlation matrix. The simulator engages the problem from a purely computational perspective. It assumes no statistical models such as copulas or parametric distributions, and can approximate the target correlations regardless of theoretical feasibility. The algorithm integrates and advances the Iman-Conover (1982) approach <doi:10.1080/03610918208812265> and the Ruscio-Kaczetow iteration (2008) <doi:10.1080/00273170802285693>. Package functions are carefully implemented in C++ for squeezing computing speed, suitable for large input in a manycore environment. Precision of the approximation and computing speed both substantially outperform various CRAN packages to date. Benchmarks are detailed in function examples. A simple heuristic algorithm is additionally designed to optimize the joint distribution in the post-simulation stage. The heuristic demonstrated good potential of achieving the same level of precision of approximation without the enhanced Iman-Conover-Ruscio-Kaczetow. The package contains a copy of Permuted Congruential Generator.
	"""
	
	cran = "SimJoint" 

	version("0.3.12", md5="763be37cb75fe26bb4f6ebd1c06b2dbb")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
