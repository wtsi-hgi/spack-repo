# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatrixmodels(RPackage):
	"""Modelling with Sparse and Dense Matrices.

	Modelling with sparse and dense 'Matrix' matrices, using modular prediction
	and response module classes."""

	cran = "MatrixModels"

	version("0.5-2", md5="4f91dd97fdb1ca38d6635c0e95af61e9")

	depends_on("r@3.6.0:", type=("build", "run"))
	depends_on("r-matrix@1.6-0:", type=("build", "run"))

