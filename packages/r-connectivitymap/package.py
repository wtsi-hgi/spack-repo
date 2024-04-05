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

	version("1.38.0", md5="bac29780256afebfd49b90f268114eaf")

	depends_on("r@2.15.1:", type=("build", "run"))

