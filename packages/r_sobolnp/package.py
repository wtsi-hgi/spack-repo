# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSobolnp(RPackage):
	"""Nonparametric Sobol Estimator with Bootstrap Bandwidth

	Algorithm to estimate the Sobol indices using a non-parametric fit of the regression curve. The bandwidth is estimated using bootstrap to reduce the finite-sample bias. The package is based on the paper Solís, M. (2018) <arXiv:1803.03333>.   
	"""
	
	homepage = "https://github.com/maikol-solis/sobolnp/"
	cran = "sobolnp" 

	version("0.1.0", md5="efc633a6b68ac16b873ef24744954654")

	depends_on("r-np", type=("build", "run"))
	depends_on("r-minqa", type=("build", "run"))
	depends_on("r-pbmcapply", type=("build", "run"))
