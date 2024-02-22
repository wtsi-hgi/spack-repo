# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRri(RPackage):
	"""Residual Randomization Inference for Regression Models

	Testing and inference for regression models using residual randomization methods. The basis of inference is an invariance assumption on the regression errors, e.g., clustered errors, or doubly-clustered errors.
	"""
	
	cran = "RRI" 

	version("1.1", md5="e5734df43b4734fbb390ae4b09aa3cfa")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
