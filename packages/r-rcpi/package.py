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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Rcpi_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Rcpi/Rcpi_1.38.0.tar.gz"]

	version("1.38.0", sha256="5a085bf6ee3b958a53a807ae558c8004f29adde466437edd92bc7984b7e0cbf2")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-gosemsim", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
