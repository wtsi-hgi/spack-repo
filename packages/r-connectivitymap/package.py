# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConnectivitymap(RPackage):
	"""Functional connections between drugs, genes and diseases as revealed by common gene-expression changes

	The Broad Institute's Connectivity Map (cmap02) is a "large reference catalogue of gene-expression data from cultured human cells perturbed with many chemicals and genetic reagents", containing more than 7000 gene expression profiles and 1300 small molecules.
	"""
	
	bioc = "ConnectivityMap"

	version("1.44.0", commit="2459a2f86cf19fa1be504cdf707752fab2eba9c5")
	version("1.38.0", commit="4b7ff6f279d8fc84c58c9471ab09e050427cc42c")

	depends_on("r@2.15.1:", type=("build", "run"))

