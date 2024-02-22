# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REasyreg(RPackage):
	"""Easy Regression

	Performs analysis of regression in simple designs with quantitative treatments, 
             including mixed models and non linear models. 
	"""
	
	cran = "easyreg" 

	version("4.0", md5="06c62bdea16e841e4e3654148a745f9b")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
