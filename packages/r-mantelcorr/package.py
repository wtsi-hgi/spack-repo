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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MantelCorr_1.72.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MantelCorr/MantelCorr_1.72.0.tar.gz"]

    version("1.78.0", tag="RELEASE_3_21")
	version("1.72.0", sha256="408a025f3d22856315b18ec4ddc99fe1fc6dfdfca7bcb8b39c8754cd3778f64b")

	depends_on("r@2.10:", type=("build", "run"))
