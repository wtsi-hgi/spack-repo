# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgntx(RPackage):
	"""Colocalization analysis of transcriptome elements in the presence of isoform heterogeneity and ambiguity

	RgnTX allows the integration of transcriptome annotations so as to model the complex alternative splicing patterns. It supports the testing of transcriptome elements without clear isoform association, which is often the real scenario due to technical limitations. It involves functions that do permutaion test for evaluating association between features and transcriptome regions.
	"""
	
	bioc = "RgnTX" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RgnTX_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RgnTX/RgnTX_1.4.0.tar.gz"]

	version("1.4.0", sha256="2dc47372b3ad28a48fcdd38c206a153f1bbe95d282008d9c7c183de79a900176")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-regioner", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-txdb-hsapiens-ucsc-hg19-knowngene", type=("build", "run"))
