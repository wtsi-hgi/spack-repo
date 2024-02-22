# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMida(RPackage):
	"""Microarray Data Analysis

	Set of functions designed to simplify transcriptome analysis and identification of marker molecules using microarrays data. The package includes a set of functions that allows performing full pipeline of analysis including data normalization, summarisation, binary classification, FDR (False Discovery Rate) multiple comparison and the definition of potential biological markers.
	"""
	
	cran = "MiDA" 

	version("0.1.2", md5="a94742dc480f863802cfe5869fdd434e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-sqn", type=("build", "run"))
