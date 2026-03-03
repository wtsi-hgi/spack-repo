# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTvm(RPackage):
	"""Time Value of Money Functions

	Functions for managing cashflows and interest rate curves.
	"""
	
	homepage = "https://bitbucket.org/juancentro/tvm"
	cran = "tvm" 

	version("0.5.2", md5="dad3e0a5f558e4755cb57a0f03f6d5ff")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
