# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGnlm(RPackage):
	"""Generalized Nonlinear Regression Models

	A variety of functions to fit linear and nonlinear
    regression with a large selection of distributions.
	"""
	
	homepage = "http://www.commanster.eu/rcode.html"
	cran = "gnlm" 

	version("1.1.1", md5="8d7bffa8b57a046db5ea1bca007da38a")

	depends_on("r@1.4:", type=("build", "run"))
	depends_on("r-rmutil", type=("build", "run"))
