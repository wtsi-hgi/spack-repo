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

	version("1.26.1", commit="72fc4b6485f16c8748ed0a5f2026f897abb3ba3d")
	version("1.20.3", commit="4b7dc4db7e54816f5fdb6de7fdef67ed835e51b5")

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
