# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBgx(RPackage):
	"""Bayesian Gene eXpression

	Bayesian integrated analysis of Affymetrix GeneChips
	"""
	
	bioc = "bgx"

	version("1.74.0", commit="0dc620dda4a7f3e81a776270df84488ee216d1f0")
	version("1.68.3", commit="a3843a52f60e16c813ca259bf6ece8d5925a1857")

	depends_on("r@2.0.1:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-affy@1.5:", type=("build", "run"))
	depends_on("r-gcrma@2.4.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("boost+random", type=("build", "link", "run"))
