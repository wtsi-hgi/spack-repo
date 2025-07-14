# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInpas(RPackage):
	"""Identify Novel Alternative PolyAdenylation Sites (PAS) from RNA-seq data

	Alternative polyadenylation (APA) is one of the important post- transcriptional regulation mechanisms which occurs in most human genes. InPAS facilitates the discovery of novel APA sites and the differential usage of APA sites from RNA-Seq data. It leverages cleanUpdTSeq to fine tune identified APA sites by removing false sites.
	"""
	
	bioc = "InPAS" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/InPAS_2.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/InPAS/InPAS_2.10.0.tar.gz"]

    version("2.16.0", tag="RELEASE_3_21")
	version("2.10.0", sha256="3e4a8db2ee1472e21f8ed71598a0e795acc80c321d14fef5d99e2d5f3aa64519")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-batchtools", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-cleanupdtseq", type=("build", "run"))
	depends_on("r-depmixs4", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-flock", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-parallelly", type=("build", "run"))
	depends_on("r-plyranges", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
