# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemicontmanova(RPackage):
	"""Multivariate ANalysis of VAriance with Ridge Regularization for
Semicontinuous High-Dimensional Data

	Implements Multivariate ANalysis Of VAriance (MANOVA) parameters' inference and test with regularization for semicontinuous high-dimensional data. The method can be applied also in presence of low-dimensional data. The p-value can be obtained through asymptotic distribution or using a permutation procedure. The package gives also the possibility to simulate this type of data. Method is described in Elena Sabbioni, Claudio Agostinelli and Alessio Farcomeni (2024) <arXiv:2401.04036>.
	"""
	
	cran = "semicontMANOVA" 

	version("0.1-8", md5="0554804ab797508bbab41b6f5dce891d")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
