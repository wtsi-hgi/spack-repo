# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrganismDplyr(RPackage):
	"""dplyr-based Access to Bioconductor Annotation Resources

	This package provides an alternative interface to Bioconductor 'annotation' resources, in particular the gene identifier mapping functionality of the 'org' packages (e.g., org.Hs.eg.db) and the genome coordinate functionality of the 'TxDb' packages (e.g., TxDb.Hsapiens.UCSC.hg38.knownGene).
	"""
	
	bioc = "Organism.dplyr" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/Organism.dplyr_1.30.1.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/Organism.dplyr/Organism.dplyr_1.30.1.tar.gz"]

	version("1.30.1", md5="b16c25c3ee5abafa1007a9c7bd731801")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-annotationfilter@1.1.3:", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dbplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
