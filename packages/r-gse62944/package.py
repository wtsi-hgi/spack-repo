# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGse62944(RPackage):
	"""GEO accession data GSE62944 as a SummarizedExperiment

	TCGA processed RNA-Seq data for 9264 tumor and 741 normal samples across 24 cancer types and made them available as GEO accession [GSE62944](http://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE62944). GSE62944 data have been parsed into a SummarizedExperiment object available in ExperimentHub.
	"""
	
	homepage = "http://bioconductor.org/packages/release/bioc/html/GSE62944.html"
	bioc = "GSE62944"

	version("1.36.0", commit="010e94ebeecd67ff4203efd95824d1aa250a91cf")
	version("1.30.0", commit="e575c133f7a2a556eae2d90c6c9a4b5fec5ce34c")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-geoquery", type=("build", "run"))

