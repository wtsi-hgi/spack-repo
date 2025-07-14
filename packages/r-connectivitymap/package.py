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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/ConnectivityMap_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/ConnectivityMap/ConnectivityMap_1.38.0.tar.gz"]

    version("1.44.0", tag="RELEASE_3_21")
	version("1.38.0", sha256="4c5be7e81dd15015973251d929e3b6d08020b492e0130d18084e187dfdacbb47")

	depends_on("r@2.15.1:", type=("build", "run"))

