# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUndo(RPackage):
	"""Unsupervised Deconvolution of Tumor-Stromal Mixed Expressions

	UNDO is an R package for unsupervised deconvolution of tumor and stromal mixed expression data. It detects marker genes and deconvolutes the mixing expression data without any prior knowledge.
	"""
	
	bioc = "UNDO" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/UNDO_1.44.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/UNDO/UNDO_1.44.0.tar.gz"]

	version("1.50.0", tag="RELEASE_3_21")
	version("1.44.0", sha256="d145f6aa55e1a8c1ffd29533573a8ffbd404caebd156e2ea782151c71cf14852")

	depends_on("r@2.15.2:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-nnls", type=("build", "run"))
