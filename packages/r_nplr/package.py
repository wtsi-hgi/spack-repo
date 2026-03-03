# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNplr(RPackage):
	"""N-Parameter Logistic Regression

	Performing drug response analyses and IC50 estimations using n-Parameter logistic regression. Can also be applied to proliferation analyses.
	"""
	
	homepage = "https://github.com/fredcommo/nplr"
	cran = "nplr" 

	version("0.1-7", md5="f957fd8b67f637704408a9617a3f78c1")

