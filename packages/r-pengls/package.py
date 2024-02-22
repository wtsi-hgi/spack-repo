# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPengls(RPackage):
	"""Fit Penalised Generalised Least Squares models

	Combine generalised least squares methodology from the nlme package for dealing with autocorrelation with penalised least squares methods from the glmnet package to deal with high dimensionality. This pengls packages glues them together through an iterative loop. The resulting method is applicable to high dimensional datasets that exhibit autocorrelation, such as spatial or temporal data.
	"""
	
	bioc = "pengls" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/pengls_1.8.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/pengls/pengls_1.8.0.tar.gz"]

	version("1.8.0", md5="7b4703b0839f4e46a97e208289a69345")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
