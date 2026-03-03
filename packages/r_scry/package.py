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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/scry_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/scry/scry_1.14.0.tar.gz"]

	version("1.14.0", md5="dbdcf37d35f52ba787d1d8d5f21e886e")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-glmpca@0.2:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biocsingular", type=("build", "run"))
