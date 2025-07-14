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

	version("1.22.0", commit="ea2b195ec23c78356d76c7310c157a44552b5349")
	version("1.16.2", commit="9459b1393dabe6799322b44d8ed48a96cc784ef8")

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
