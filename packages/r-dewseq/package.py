# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDewseq(RPackage):
	"""Differential Expressed Windows Based on Negative Binomial Distribution

	DEWSeq is a sliding window approach for the analysis of differentially enriched binding regions eCLIP or iCLIP next generation sequencing data.
	"""
	
	homepage = "https://github.com/EMBL-Hentze-group/DEWSeq/"
	bioc = "DEWSeq" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/DEWSeq_1.16.2.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/DEWSeq/DEWSeq_1.16.2.tar.gz"]

	version("1.16.2", md5="4164c3c7d4967586861e0c2d40815ec5")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-data-table@1.11.8:", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
