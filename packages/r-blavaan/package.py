# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlavaan(RPackage):
	"""Bayesian Latent Variable Analysis.

	Fit a variety of Bayesian latent variable models, including confirmatory factor
	analysis, structural equation models, and latent growth curve models.
	References: Merkle & Rosseel (2018) <doi:10.18637/jss.v085.i04>; Merkle et al.
	(2021) <doi:10.18637/jss.v100.i06>."""

	cran = "blavaan"

	license("GPL-3.0-or-later")

	version("0.5-3", md5="fc9090278c63747c904661506244a6e0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp@0.12.15:", type=("build", "run"))
	depends_on("r-lavaan@0.6.17:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-nonnest2@0.5.5:", type=("build", "run"))
	depends_on("r-loo@2:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@1.5:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-bayesplot", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-tmvnsim", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
	depends_on("r-bh@1.69:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.4:", type=("build", "run"))
