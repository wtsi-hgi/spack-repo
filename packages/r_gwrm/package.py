# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwrm(RPackage):
	"""Generalized Waring Regression Model for Count Data

	Statistical functions to fit, validate and describe a Generalized
    Waring Regression Model (GWRM).
	"""
	
	cran = "GWRM" 

	version("2.1.0.4", md5="9c6e0150ec78ada73092fcb944663bb5")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
