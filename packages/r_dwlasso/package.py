# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDwlasso(RPackage):
	"""Degree Weighted Lasso

	Infers networks with hubs using degree weighted Lasso method.
	"""
	
	cran = "DWLasso" 

	version("1.1", md5="01072d716e88f338d62776e2de26edd5")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-hglasso", type=("build", "run"))
