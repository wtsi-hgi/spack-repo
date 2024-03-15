# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSitadela(RPackage):
	"""An R package for the easy provision of simple but complete tab-delimited genomic annotation from a variety of sources and organisms

	Provides an interface to build a unified database of genomic annotations and their coordinates (gene, transcript and exon levels). It is aimed to be used when simple tab-delimited annotations (or simple GRanges objects) are required instead of the more complex annotation Bioconductor packages. Also useful when combinatorial annotation elements are reuired, such as RefSeq coordinates with Ensembl biotypes. Finally, it can download, construct and handle annotations with versioned genes and transcripts (where available, e.g. RefSeq and latest Ensembl). This is particularly useful in precision medicine applications where the latter must be reported.
	"""
	
	homepage = "https://github.com/pmoulos/sitadela"
	bioc = "sitadela" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/sitadela_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/sitadela/sitadela_1.10.0.tar.gz"]

	version("1.10.0", md5="109b3096c37f30906c8c009097e45c59")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
