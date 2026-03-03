# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFwdselect(RPackage):
	"""Selecting Variables in Regression Models

	A simple method
    to select the best model or best subset of variables using
    different types of data (binary, Gaussian or Poisson) and
    applying it in different contexts (parametric or non-parametric).
	"""
	
	homepage = "http://cran.r-project.org/package=FWDselect"
	cran = "FWDselect" 

	version("2.1.0", md5="a987853a8e590c7fac9e098d36645775")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-cvtools", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
