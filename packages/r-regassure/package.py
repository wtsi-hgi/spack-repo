# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegassure(RPackage):
	"""Streamlined Integration of Regression Assumption

	It streamlines the evaluation of regression model
    assumptions, enhancing result reliability. With integrated tools for
    assessing key aspects like linearity, homoscedasticity, and more. It's
    a valuable asset for researchers and analysts working with regression
    models.
	"""
	
	cran = "RegAssure" 

	version("1.0.0", md5="352939179ec4c28933f292a624a3c7de")

	depends_on("r-brant", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
