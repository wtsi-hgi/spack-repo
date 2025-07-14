# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScry(RPackage):
	"""Small-Count Analysis Methods for High-Dimensional Data

	Many modern biological datasets consist of small counts that are not well fit by standard linear-Gaussian methods such as principal component analysis. This package provides implementations of count-based feature selection and dimension reduction algorithms. These methods can be used to facilitate unsupervised analysis of any high-dimensional data such as single-cell RNA-seq.
	"""
	
	homepage = "https://bioconductor.org/packages/scry.html"
	bioc = "scry"

	version("1.20.0", commit="c6878b3f714b5e87953ab8a1a5f05ae4c6cc3ab6")
	version("1.14.0", commit="d43e3ffc3f47d57eadb98a181314cdc99c7fe6e8")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-glmpca@0.2:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biocsingular", type=("build", "run"))
