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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/GSE62944_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/GSE62944/GSE62944_1.30.0.tar.gz"]

    version("1.36.0", tag="RELEASE_3_21")
	version("1.30.0", sha256="97f79656ba27c3f3649e0f9ea967deb08e65ced1d8015f2773013af3a4249e0f", url="https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/GSE62944_1.30.0.tar.gz")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-geoquery", type=("build", "run"))

