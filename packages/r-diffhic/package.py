# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiffhic(RPackage):
	"""Differential Analyis of Hi-C Data

	Detects differential interactions across biological conditions in a Hi-C experiment. Methods are provided for read alignment and data pre-processing into interaction counts. Statistical analysis is based on edgeR and supports normalization and filtering. Several visualization options are also available.
	"""
	
	bioc = "diffHic" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/diffHic_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/diffHic/diffHic_1.34.0.tar.gz"]

	version("1.34.0", sha256="c05b50a5091a128ddda24e1af44b2bc88084944e1f4d8a6e5d075774375f99b5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-interactionset", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-rhtslib@1.13.1:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-csaw", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-zlibbioc", type=("build", "run"))
	depends_on("curl", type=("build", "link", "run"))
	depends_on("bzip2", type=("build", "link", "run"))
	depends_on("xz", type=("build", "link", "run"))
	depends_on("zlib", type=("build", "link", "run"))
