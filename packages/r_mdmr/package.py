# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMdmr(RPackage):
	"""Multivariate Distance Matrix Regression

	Allows users to conduct multivariate distance matrix regression using analytic p-values and compute measures of effect size. For details on the method, see McArtor, Lubke, & Bergeman (2017) <doi:10.1007/s11336-016-9527-8>.
	"""
	
	homepage = "http://github.com/dmcartor/mdmr"
	cran = "MDMR" 

	version("0.5.1", md5="a44413a4e42e085c7c0e3e1c89564096")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
