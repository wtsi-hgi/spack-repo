# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnico(RPackage):
	"""Unified Cross-Omics Deconvolution

	UNIfied Cross-Omics deconvolution (Unico) deconvolves
    standard 2-dimensional bulk matrices of samples by features into a
    3-dimensional tensors representing samples by features by cell types.
    Unico stands out as the first principled model-based deconvolution
    method that is theoretically justified for any heterogeneous genomic
    data. For more details see Chen and Rahmani et al. (2024)
    <doi:10.1101/2024.01.27.577588>.
	"""
	
	homepage = "https://cozygene.github.io/Unico/"
	cran = "Unico" 

	version("0.1.0", md5="408a4808c8d01d09fd0fd0d0b1c3de18")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-compositions", type=("build", "run"))
	depends_on("r-config", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-futile-logger", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-testit", type=("build", "run"))
