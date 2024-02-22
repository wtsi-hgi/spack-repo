# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR02pro(RPackage):
	"""R Programming: Zero to Pro

	This is a companion package of the book "R Programming: Zero to Pro"  <https://r02pro.github.io/>. It contains the datasets used in the book and provides interactive exercises corresponding to the book. It covers a wide range of topics including visualization, data transformation, tidying data, data input and output.
	"""
	
	homepage = "https://r02pro.github.io/"
	cran = "r02pro" 

	version("0.2", md5="d99232dcf800b21c68cf9b0a354fbb7a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-learnr", type=("build", "run"))
