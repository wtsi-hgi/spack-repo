# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIbbig(RPackage):
	"""Iterative Binary Biclustering of Genesets

	iBBiG is a bi-clustering algorithm which is optimizes for binary data analysis. We apply it to meta-gene set analysis of large numbers of gene expression datasets. The iterative algorithm extracts groups of phenotypes from multiple studies that are associated with similar gene sets. iBBiG does not require prior knowledge of the number or scale of clusters and allows discovery of clusters with diverse sizes
	"""
	
	homepage = "http://bcb.dfci.harvard.edu/~aedin/publications/"
	bioc = "iBBiG" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/iBBiG_1.46.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/iBBiG/iBBiG_1.46.0.tar.gz"]

    version("1.52.0", tag="RELEASE_3_21")
	version("1.46.0", sha256="5aaa1252ef2969ac5c9fb1f14be2049baf1938c165a432dee20b0f8abc1ba896")

	depends_on("r-biclust", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
