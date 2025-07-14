# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpitxdb(RPackage):
	"""Storing and accessing epitranscriptomic information using the AnnotationDbi interface

	EpiTxDb facilitates the storage of epitranscriptomic information. More specifically, it can keep track of modification identity, position, the enzyme for introducing it on the RNA, a specifier which determines the position on the RNA to be modified and the literature references each modification is associated with.
	"""
	
	homepage = "https://github.com/FelixErnst/EpiTxDb"
	bioc = "EpiTxDb" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/EpiTxDb_1.14.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/EpiTxDb/EpiTxDb_1.14.1.tar.gz"]

    version("1.20.0", tag="RELEASE_3_21")
	version("1.14.1", sha256="ad425f358f3cd7b31efb8c29069b204bd9b83d90cf13638dd92f704826c78762")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-modstrings", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-trnadbimport", type=("build", "run"))
