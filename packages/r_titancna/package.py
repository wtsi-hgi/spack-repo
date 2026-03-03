# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTitancna(RPackage):
	"""Subclonal copy number and LOH prediction from whole genome sequencing of tumours

	Hidden Markov model to segment and predict regions of subclonal copy number alterations (CNA) and loss of heterozygosity (LOH), and estimate cellular prevalence of clonal clusters in tumour whole genome sequencing data.
	"""
	
	homepage = "https://github.com/gavinha/TitanCNA"
	bioc = "TitanCNA" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/TitanCNA_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/TitanCNA/TitanCNA_1.40.0.tar.gz"]

	version("1.40.0", md5="ce40de587ae35a22c583019e6a85dbc6")

	depends_on("r@3.5.1:", type=("build", "run"))
	depends_on("r-biocgenerics@0.31.6:", type=("build", "run"))
	depends_on("r-iranges@2.6.1:", type=("build", "run"))
	depends_on("r-genomicranges@1.24.3:", type=("build", "run"))
	depends_on("r-variantannotation@1.18.7:", type=("build", "run"))
	depends_on("r-foreach@1.4.3:", type=("build", "run"))
	depends_on("r-genomeinfodb@1.8.7:", type=("build", "run"))
	depends_on("r-data-table@1.10.4:", type=("build", "run"))
	depends_on("r-dplyr@0.5:", type=("build", "run"))
