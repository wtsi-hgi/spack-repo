# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTximeta(RPackage):
	"""Transcript Quantification Import with Automatic Metadata

	Transcript quantification import from Salmon and other quantifiers with automatic attachment of transcript ranges and release information, and other associated metadata. De novo transcriptomes can be linked to the appropriate sources with linkedTxomes and shared for computational reproducibility.
	"""
	
	homepage = "https://github.com/thelovelab/tximeta"
	bioc = "tximeta" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/tximeta_1.20.3.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/tximeta/tximeta_1.20.3.tar.gz"]

	version("1.20.3", sha256="c70f28a180880efe33aaae84b4ddfe234ace34b0a3fc87cc15865d0df72c9d42")

	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-tximport", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-ensembldb", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
