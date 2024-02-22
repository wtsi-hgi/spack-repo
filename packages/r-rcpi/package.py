# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcpi(RPackage):
	"""Molecular Informatics Toolkit for Compound-Protein Interaction in Drug Discovery

	A molecular informatics toolkit with an integration of bioinformatics and chemoinformatics tools for drug discovery.
	"""
	
	homepage = "https://nanx.me/Rcpi/"
	bioc = "Rcpi" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/Rcpi_1.38.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/Rcpi/Rcpi_1.38.0.tar.gz"]

	version("1.38.0", md5="2f3697ca19200881f65d7d37f3d34e33")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-gosemsim", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
