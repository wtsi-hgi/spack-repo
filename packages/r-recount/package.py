# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRecount(RPackage):
	"""Explore and download data from the recount project

	Explore and download data from the recount project available at https://jhubiostatistics.shinyapps.io/recount/. Using the recount package you can download RangedSummarizedExperiment objects at the gene, exon or exon-exon junctions level, the raw counts, the phenotype metadata used, the urls to the sample coverage bigWig files or the mean coverage bigWig file for a particular study. The RangedSummarizedExperiment objects can be used by different packages for performing differential expression analysis. Using http://bioconductor.org/packages/derfinder you can perform annotation-agnostic differential expression analyses with the data from the recount project as described at http://www.nature.com/nbt/journal/v35/n4/full/nbt.3838.html.
	"""
	
	homepage = "https://github.com/leekgroup/recount"
	bioc = "recount" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/recount_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/recount/recount_1.28.0.tar.gz"]

	version("1.34.0", tag="RELEASE_3_21")
	version("1.28.0", sha256="ef6037f3fccee7a3b5e823202753b3d490173ea4e401e0668af364e64976c2da")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-derfinder", type=("build", "run"))
	depends_on("r-downloader", type=("build", "run"))
	depends_on("r-geoquery", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-rentrez", type=("build", "run"))
	depends_on("r-rtracklayer@1.35.3:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
