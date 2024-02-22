# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPeca(RPackage):
	"""Probe-level Expression Change Averaging

	Calculates Probe-level Expression Change Averages (PECA) to identify differential expression in Affymetrix gene expression microarray studies or in proteomic studies using peptide-level mesurements respectively.
	"""
	
	bioc = "PECA" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/PECA_1.38.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/PECA/PECA_1.38.0.tar.gz"]

	version("1.38.0", md5="43aed7fc555cb6ccbf70335add80f6dc")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rots", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-aroma-affymetrix", type=("build", "run"))
	depends_on("r-aroma-core", type=("build", "run"))
