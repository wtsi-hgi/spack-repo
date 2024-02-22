# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLtsspca(RPackage):
	"""Sparse Principal Component Based on Least Trimmed Squares

	Implementation of robust and sparse PCA algorithm of Wang and Van Aelst (2019) <DOI:10.1080/00401706.2019.1671234>.
	"""
	
	cran = "ltsspca" 

	version("0.1.0", md5="807350f143d55efa2f1f6d987368cfc4")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
