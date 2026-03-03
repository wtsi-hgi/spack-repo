# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsc(RPackage):
	"""Robust and Sparse Correlation Matrix

	Performs robust and sparse correlation matrix estimation. Robustness is achieved based on a simple robust pairwise correlation estimator, while sparsity is obtained based on thresholding. The optimal thresholding is tuned via cross-validation. See Serra, Coretto, Fratello and Tagliaferri (2018) <doi:10.1093/bioinformatics/btx642>.
	"""
	
	cran = "RSC" 

	version("2.0.4", md5="0359722818904619924225abf948de78")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
