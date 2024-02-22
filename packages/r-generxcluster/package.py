# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenerxcluster(RPackage):
	"""gRx Differential Clustering

	Detect Differential Clustering of Genomic Sites such as gene therapy integrations.  The package provides some functions for exploring genomic insertion sites originating from two different sources. Possibly, the two sources are two different gene therapy vectors.  Vectors are preferred that target sensitive regions less frequently, motivating the search for localized clusters of insertions and comparison of the clusters formed by integration of different vectors.  Scan statistics allow the discovery of spatial differences in clustering and calculation of False Discovery Rates (FDRs) providing statistical methods for comparing retroviral vectors. A scan statistic for comparing two vectors using multiple window widths to detect clustering differentials and compute FDRs is implemented here.
	"""
	
	bioc = "geneRxCluster" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/geneRxCluster_1.38.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/geneRxCluster/geneRxCluster_1.38.0.tar.gz"]

	version("1.38.0", md5="61f7d4c5cd314cf84f8648b3097f65b1")

	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
