# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomicfeatures(RPackage):
	"""Conveniently import and query gene models.

	A set of tools and methods for making and manipulating transcript
	centric annotations. With these tools the user can easily download the
	genomic locations of the transcripts, exons and cds of a given organism,
	from either the UCSC Genome Browser or a BioMart database (more sources
	will be supported in the future). This information is then stored in a
	local database that keeps track of the relationship between transcripts,
	exons, cds and genes. Flexible methods are provided for extracting the
	desired features in a convenient format."""

	bioc = "GenomicFeatures"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GenomicFeatures_1.54.3.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GenomicFeatures/GenomicFeatures_1.54.3.tar.gz"]

	version("1.54.3", md5="ff1db6c7968d616ad62d011206144975")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocgenerics@0.1:", type=("build", "run"))
	depends_on("r-s4vectors@0.17.29:", type=("build", "run"))
	depends_on("r-iranges@2.13.23:", type=("build", "run"))
	depends_on("r-genomeinfodb@1.35.8:", type=("build", "run"))
	depends_on("r-genomicranges@1.31.17:", type=("build", "run"))
	depends_on("r-annotationdbi@1.41.4:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rsqlite@2:", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-xvector@0.19.7:", type=("build", "run"))
	depends_on("r-biostrings@2.47.6:", type=("build", "run"))
	depends_on("r-biocio", type=("build", "run"))
	depends_on("r-rtracklayer@1.51.5:", type=("build", "run"))
	depends_on("r-biomart@2.58.2:", type=("build", "run"))
	depends_on("r-biobase@2.15.1:", type=("build", "run"))
