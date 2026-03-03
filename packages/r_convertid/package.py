# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConvertid(RPackage):
	"""Convert Gene IDs Between Each Other and Fetch Annotations from
Biomart

	Gene Symbols or Ensembl Gene IDs are converted using the Bimap interface in 'AnnotationDbi' in convertId2() but
    that function is only provided as fallback mechanism for the most common use cases in data analysis. The main function
    in the package is convert.bm() which queries BioMart using the full capacity of the API provided through the
    'biomaRt' package. Presets and defaults are provided for convenience but all "marts", "filters" and "attributes"
    can be set by the user. Function convert.alias() converts Gene Symbols to Aliases and vice versa and function likely_symbol()
    attempts to determine the most likely current Gene Symbol.
	"""
	
	cran = "convertid" 

	version("0.1.8", md5="797a9b0ca028d0db6869f991d8dac00e")

	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-org-mm-eg-db", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
