# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatrixcorrelation(RPackage):
	"""Matrix Correlation Coefficients

	Computation and visualization of matrix correlation coefficients.
    The main method is the Similarity of Matrices Index, while various related
    measures like r1, r2, r3, r4, Yanai's GCD, RV, RV2, adjusted RV, Rozeboom's
    linear correlation and Coxhead's coefficient are included
    for comparison and flexibility.
	"""
	
	homepage = "https://github.com/khliland/MatrixCorrelation/"
	cran = "MatrixCorrelation" 

	version("0.10.0", md5="0082ae6056ce142743c9caf707964b49")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
