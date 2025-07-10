# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBanocc(RPackage):
	"""Bayesian ANalysis Of Compositional Covariance

	BAnOCC is a package designed for compositional data, where each sample sums to one. It infers the approximate covariance of the unconstrained data using a Bayesian model coded with `rstan`. It provides as output the `stanfit` object as well as posterior median and credible interval estimates for each correlation element.
	"""
	
	bioc = "banocc" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/banocc_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/banocc/banocc_1.26.0.tar.gz"]

	version("1.26.0", sha256="f7c1d389eb39421a23df556e097bee3d6a800fc2a3bc6288e9428fbee68fd578")

	depends_on("r@3.5.1:", type=("build", "run"))
	depends_on("r-rstan@2.17.4:", type=("build", "run"))
	depends_on("r-coda@0.18.1:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
