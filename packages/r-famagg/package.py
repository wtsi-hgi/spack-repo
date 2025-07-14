# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFamagg(RPackage):
	"""Pedigree Analysis and Familial Aggregation

	Framework providing basic pedigree analysis and plotting utilities as well as a variety of methods to evaluate familial aggregation of traits in large pedigrees.
	"""
	
	homepage = "https://github.com/EuracBiomedicalResearch/FamAgg"
	bioc = "FamAgg" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/FamAgg_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/FamAgg/FamAgg_1.30.0.tar.gz"]

    version("1.36.0", tag="RELEASE_3_21")
	version("1.30.0", sha256="1d4977c26fbcf5a06603fcabee605cd8265449328128590667f0c7cde3a77082")

	depends_on("r-kinship2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-gap@1.1.17:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
