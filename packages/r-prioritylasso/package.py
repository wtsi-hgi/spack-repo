# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrioritylasso(RPackage):
	"""Analyzing Multiple Omics Data with an Offset Approach

	Fits successive Lasso models for several blocks of (omics) data with different priorities and takes the predicted values as an offset for the next block. Also offers options to deal with block-wise missingness in multi-omics data.
	"""
	
	cran = "prioritylasso" 

	version("0.3.1", md5="1eda3ef291d1417bce4f516b79493ec4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
