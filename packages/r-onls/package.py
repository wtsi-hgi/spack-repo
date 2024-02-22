# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnls(RPackage):
	"""Orthogonal Nonlinear Least-Squares Regression

	Fits two-dimensional data by means of orthogonal nonlinear least-squares using Levenberg-Marquardt minimization and provides functionality for fit diagnostics and plotting.
	"""
	
	cran = "onls" 

	version("0.1-2", md5="d07082fed8dba124921ce15cc3d6df87")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
