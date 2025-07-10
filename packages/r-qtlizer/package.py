# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQtlizer(RPackage):
	"""Comprehensive QTL annotation of GWAS results

	This R package provides access to the Qtlizer web server. Qtlizer annotates lists of common small variants (mainly SNPs) and genes in humans with associated changes in gene expression using the most comprehensive database of published quantitative trait loci (QTLs).
	"""
	
	bioc = "Qtlizer" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Qtlizer_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Qtlizer/Qtlizer_1.16.0.tar.gz"]

	version("1.16.0", sha256="f495e677887845f38c37abbf7e36f8d35f791b33a1300d01eb568817df559b3d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
