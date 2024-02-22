# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrcutt(RPackage):
	"""Estimate Procedure in Case of First Order Autocorrelation

	Solve first order autocorrelation problems using an iterative method. This procedure estimates both autocorrelation and beta coefficients recursively until we reach the convergence (8th decimal as default). The residuals are computed after estimating Beta using EGLS approach and Rho is estimated using the previous residuals.
	"""
	
	cran = "orcutt" 

	version("2.3", md5="7d290bc57df3c2408cbf9d01313f26a5")

	depends_on("r-lmtest", type=("build", "run"))
