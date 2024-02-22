# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUniprotWs(RPackage):
	"""R Interface to UniProt Web Services

	The Universal Protein Resource (UniProt) is a comprehensive resource for protein sequence and annotation data. This package provides a collection of functions for retrieving, processing, and re-packaging UniProt web services. The package makes use of UniProt's modernized REST API and allows mapping of identifiers accross different databases.
	"""
	
	homepage = "https://github.com/Bioconductor/UniProt.ws"
	bioc = "UniProt.ws" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/UniProt.ws_2.42.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/UniProt.ws/UniProt.ws_2.42.0.tar.gz"]

	version("2.42.0", md5="47d9ee4038c5dcaf66229e4e1e07c052")

	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-biocbaseutils", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-httpcache", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rjsoncons", type=("build", "run"))
