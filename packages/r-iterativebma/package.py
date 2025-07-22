# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIterativebma(RPackage):
	"""The Iterative Bayesian Model Averaging (BMA) algorithm

	The iterative Bayesian Model Averaging (BMA) algorithm is a variable selection and classification algorithm with an application of classifying 2-class microarray samples, as described in Yeung, Bumgarner and Raftery (Bioinformatics 2005, 21: 2394-2402).
	"""
	
	homepage = "http://faculty.washington.edu/kayee/research.html"
	bioc = "iterativeBMA" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/iterativeBMA_1.60.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/iterativeBMA/iterativeBMA_1.60.0.tar.gz"]

	version("1.60.0", sha256="da16e7d1b3f2c98f621613c9e9e44cc75e40bc76809a22264f206e326f755c11")

	depends_on("r-bma", type=("build", "run"))
	depends_on("r-leaps", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
