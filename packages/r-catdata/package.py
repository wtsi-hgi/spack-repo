# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCatdata(RPackage):
	"""Categorical Data

	This R-package contains examples from the book "Regression for Categorical Data", Tutz 2012, Cambridge University Press. The names of the examples refer to the chapter and the data set that is used. 
	"""
	
	cran = "catdata" 

	version("1.2.4", md5="f01789b27f0514e073d456f6875e23d7")

	depends_on("r-mass", type=("build", "run"))
