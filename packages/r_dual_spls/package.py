# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDualSpls(RPackage):
	"""Dual Sparse Partial Least Squares Regression

	Provides a series of functions for fitting a dual sparse partial least squares (Dual-SPLS) regression. These functions differ by the choice of the underlying norm. 
	"""
	
	cran = "dual.spls" 

	version("0.1.4", md5="fbf35b18bcc4538ee5a3c901c6b301cf")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-pdist", type=("build", "run"))
