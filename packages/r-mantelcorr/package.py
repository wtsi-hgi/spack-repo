# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMantelcorr(RPackage):
	"""Compute Mantel Cluster Correlations

	Computes Mantel cluster correlations from a (p x n) numeric data matrix (e.g. microarray gene-expression data).
	"""
	
	bioc = "MantelCorr"

	version("1.78.0", commit="fdc95782a19cef46869e36d1650b050992389525")
	version("1.72.0", commit="b41ad7417ceaea7e37f1054142746bb7ba7887df")

	depends_on("r@2.10:", type=("build", "run"))
