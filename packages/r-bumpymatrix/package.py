# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBumpymatrix(RPackage):
	"""Bumpy Matrix of Non-Scalar Objects

	Implements the BumpyMatrix class and several subclasses for holding non-scalar objects in each entry of the matrix. This is akin to a ragged array but the raggedness is in the third dimension, much like a bumpy surface - hence the name. Of particular interest is the BumpyDataFrameMatrix, where each entry is a Bioconductor data frame. This allows us to naturally represent multivariate data in a format that is compatible with two-dimensional containers like the SummarizedExperiment and MultiAssayExperiment objects.
	"""
	
	homepage = "https://bioconductor.org/packages/BumpyMatrix"
	bioc = "BumpyMatrix" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BumpyMatrix_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BumpyMatrix/BumpyMatrix_1.10.0.tar.gz"]

	version("1.10.0", sha256="59d0ffa888891010b4a42ede246bada833f8c634eb27a07db5692cdea53b8845")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
