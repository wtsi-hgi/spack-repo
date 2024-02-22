# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTmvmixnorm(RPackage):
	"""Sampling from Truncated Multivariate Normal and t Distributions

	Efficient sampling of truncated multivariate (scale) mixtures of normals under linear inequality constraints is nontrivial due to the analytically intractable normalizing constant. Meanwhile, traditional methods may subject to numerical issues, especially when the dimension is high and dependence is strong.    Algorithms proposed by Li and Ghosh (2015) <doi: 10.1080/15598608.2014.996690> are adopted for overcoming difficulties in simulating truncated distributions. Efficient rejection sampling for simulating truncated univariate normal distribution is included in the package, which shows superiority in terms of acceptance rate and numerical stability compared to existing methods and R packages. An efficient function for sampling from truncated multivariate normal distribution subject to convex polytope restriction regions based on Gibbs sampler for conditional truncated univariate distribution is provided. By extending the sampling method, a function for sampling truncated multivariate Student's t distribution is also developed.     Moreover, the proposed method and computation remain valid for high dimensional and strong dependence scenarios. Empirical results in Li and Ghosh (2015) <doi: 10.1080/15598608.2014.996690> illustrated the superior performance in terms of various criteria (e.g. mixing and integrated auto-correlation time).
	"""
	
	cran = "tmvmixnorm" 

	version("1.1.1", md5="2ae27082e9f8cacc59a64cbb04e53c4c")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
