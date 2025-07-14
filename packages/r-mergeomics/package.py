# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMergeomics(RPackage):
	"""Integrative network analysis of omics data

	The Mergeomics pipeline serves as a flexible framework for integrating multidimensional omics-disease associations, functional genomics, canonical pathways and gene-gene interaction networks to generate mechanistic hypotheses. It includes two main parts, 1) Marker set enrichment analysis (MSEA); 2) Weighted Key Driver Analysis (wKDA).
	"""
	
	bioc = "Mergeomics" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Mergeomics_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Mergeomics/Mergeomics_1.30.0.tar.gz"]

    version("1.36.0", tag="RELEASE_3_21")
	version("1.30.0", sha256="03480d2a56911e31333b3eece4d8a1d2b5418c051c276d3017e0195f99226260")

	depends_on("r@3.0.1:", type=("build", "run"))
