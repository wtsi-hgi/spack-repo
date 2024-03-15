# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnsembldb(RPackage):
	"""Utilities to create and use Ensembl-based annotation databases.

	The package provides functions to create and use transcript centric
	annotation databases/packages. The annotation for the databases are
	directly fetched from Ensembl using their Perl API. The functionality
	and data is similar to that of the TxDb packages from the
	GenomicFeatures package, but, in addition to retrieve all
	gene/transcript models and annotations from the database, ensembldb
	provides a filter framework allowing to retrieve annotations for
	specific entries like genes encoded on a chromosome region or transcript
	models of lincRNA genes. EnsDb databases built with ensembldb contain
	also protein annotations and mappings between proteins and their
	encoding transcripts. Finally, ensembldb provides functions to map
	between genomic, transcript and protein coordinates."""

	bioc = "ensembldb"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ensembldb_2.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ensembldb/ensembldb_2.26.0.tar.gz"]

	version("2.26.0", md5="0ad7a33ad9592f54e39d647195aa4c91")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocgenerics@0.15.10:", type=("build", "run"))
	depends_on("r-genomicranges@1.31.18:", type=("build", "run"))
	depends_on("r-genomicfeatures@1.49.6:", type=("build", "run"))
	depends_on("r-annotationfilter@1.5.2:", type=("build", "run"))
	depends_on("r-rsqlite@1.1:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-annotationdbi@1.31.19:", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-s4vectors@0.23.10:", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-iranges@2.13.24:", type=("build", "run"))
	depends_on("r-protgenerics", type=("build", "run"))
	depends_on("r-biostrings@2.47.9:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
