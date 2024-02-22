# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApi2lm(RPackage):
	"""Functions and Data Sets for the Book "A Progressive Introduction
to Linear Models"

	Simplifies aspects of linear regression analysis, particularly simultaneous inference. Additionally, supports "A Progressive Introduction to Linear Models" by Joshua French (<https://jfrench.github.io/LinearRegression/>).
	"""
	
	cran = "api2lm" 

	version("0.2", md5="475d45c8cea4deeca904eb1c87bebece")

	depends_on("r@3.5:", type=("build", "run"))
