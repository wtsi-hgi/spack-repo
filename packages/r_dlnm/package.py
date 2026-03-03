# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDlnm(RPackage):
	"""Distributed Lag Non-Linear Models

	Collection of functions for distributed lag linear and non-linear models.
	"""
	
	homepage = "https://github.com/gasparrini/dlnm"
	cran = "dlnm" 

	version("2.4.7", md5="4edbc95162dc56aa7c552d2a65e3edcf")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-tsmodel", type=("build", "run"))
