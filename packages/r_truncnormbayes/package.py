# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTruncnormbayes(RPackage):
	"""Estimates Moments for a Truncated Normal Distribution using
'Stan'

	Finds the posterior modes for the mean and standard deviation for a
  truncated normal distribution with one or two known truncation points.
  The method used extends Bayesian methods for parameter estimation for a singly
  truncated normal distribution under the Jeffreys prior (see Zhou X,
  Giacometti R, Fabozzi FJ, Tucker AH (2014). "Bayesian estimation of truncated
  data with applications to operational risk measurement".
  <doi:10.1080/14697688.2012.752103>). This package additionally allows for a
  doubly truncated normal distribution.
	"""
	
	homepage = "https://github.com/mathurlabstanford/truncnormbayes"
	cran = "truncnormbayes" 

	version("0.0.3", md5="da4bafc86076b79a6593cc09dc332c0e")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-rstantools@2.2:", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
