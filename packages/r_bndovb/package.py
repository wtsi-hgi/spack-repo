# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBndovb(RPackage):
	"""Bounding Omitted Variable Bias Using Auxiliary Data

	Functions to implement a Hwang(2021) <doi:10.2139/ssrn.3866876> estimator, which bounds an omitted variable bias using auxiliary data.
	"""
	
	cran = "bndovb" 

	version("1.1", md5="a7dec95f4a9f1f10c2590d612df90eae")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-np", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-factormodel", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
