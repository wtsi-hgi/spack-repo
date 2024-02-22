# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRecount3(RPackage):
	"""Explore and download data from the recount3 project

	The recount3 package enables access to a large amount of uniformly processed RNA-seq data from human and mouse. You can download RangedSummarizedExperiment objects at the gene, exon or exon-exon junctions level with sample metadata and QC statistics. In addition we provide access to sample coverage BigWig files.
	"""
	
	homepage = "https://github.com/LieberInstitute/recount3"
	bioc = "recount3" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/recount3_1.12.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/recount3/recount3_1.12.0.tar.gz"]

	version("1.12.0", md5="0e3b0229faa614fbbc49547e44b342d7", url="https://www.bioconductor.org/packages/release/bioc/src/contrib/recount3_1.12.0.tar.gz")

	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-sessioninfo", type=("build", "run"))
