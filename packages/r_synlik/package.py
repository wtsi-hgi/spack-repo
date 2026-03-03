# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSynlik(RPackage):
	"""Synthetic Likelihood Methods for Intractable Likelihoods

	Framework to perform synthetic likelihood inference
    for models where the likelihood function is unavailable or
    intractable.
	"""
	
	homepage = "http://mfasiolo.github.io/synlik_release/"
	cran = "synlik" 

	version("0.1.6", md5="a00e007065b1ed3d99b2c194ae5d783f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
