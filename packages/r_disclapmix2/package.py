# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDisclapmix2(RPackage):
	"""Mixtures of Discrete Laplace Distributions using Numerical
Optimisation

	Fit a mixture of Discrete Laplace distributions using plain numerical optimisation. This package has similar applications as the 'disclapmix' package that uses an EM algorithm.
	"""
	
	cran = "disclapmix2" 

	version("0.6.1", md5="70a3e256bcd242686573e2c109951a91", url="https://cran.r-project.org/src/contrib/disclapmix2_0.6.1.tar.gz")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
