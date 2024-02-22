# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDenoiser(RPackage):
	"""Regularized Low Rank Matrix Estimation

	Estimate a low rank matrix from noisy data using singular values
    thresholding and shrinking functions. Impute missing values with matrix completion. The method is described in <arXiv:1602.01206>.
	"""
	
	cran = "denoiseR" 

	version("1.0.2", md5="e7793bcca3df61ba506e0912ab6ec81f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
