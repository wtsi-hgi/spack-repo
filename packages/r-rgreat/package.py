# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgreat(RPackage):
	"""GREAT Analysis - Functional Enrichment on Genomic Regions

	GREAT (Genomic Regions Enrichment of Annotations Tool) is a type of functional enrichment analysis directly performed on genomic regions. This package implements the GREAT algorithm (the local GREAT analysis), also it supports directly interacting with the GREAT web service (the online GREAT analysis). Both analysis can be viewed by a Shiny application. rGREAT by default supports more than 600 organisms and a large number of gene set collections, as well as self-provided gene sets and organisms from users. Additionally, it implements a general method for dealing with background regions.
	"""
	
	homepage = "https://github.com/jokergoo/rGREAT"
	bioc = "rGREAT" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/rGREAT_2.4.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/rGREAT/rGREAT_2.4.0.tar.gz"]

	version("2.4.0", md5="89ee57f3429887678846bba965ce84dc")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-getoptlong@0.0.9:", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-globaloptions", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-txdb-hsapiens-ucsc-hg19-knowngene", type=("build", "run"))
	depends_on("r-txdb-hsapiens-ucsc-hg38-knowngene", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
