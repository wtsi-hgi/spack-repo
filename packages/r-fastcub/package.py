# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastcub(RPackage):
	"""Fast EM and Best-Subset Selection for CUB Models for Rating Data

	For ordinal rating data, consider the accelerated Expectation-Maximization algorithm to estimate and test models within the family of CUB models (where CUB stands for Combination of a discrete Uniform and a shifted Binomial distributions). The procedure is built upon Louis' identity for the observed information matrix.  Best-subset variable selection for CUB regression models is then implemented on such basis. The methods here implemented are illustrated and discussed in the preprint available from Researchgate by Simone R. (2020) <https://tinyurl.com/vvk563e>.
	"""
	
	cran = "FastCUB" 

	version("0.0.2", md5="481c248e1f6882af1e478abd928ca59a")

	depends_on("r@2.15.2:", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-cub", type=("build", "run"))
