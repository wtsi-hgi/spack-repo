# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBreakdown(RPackage):
	"""Model Agnostic Explainers for Individual Predictions

	Model agnostic tool for decomposition of predictions from black boxes.
    Break Down Table shows contributions of every variable to a final prediction. 
    Break Down Plot presents variable contributions in a concise graphical way. 
    This package work for binary classifiers and general regression models. 
	"""
	
	homepage = "https://pbiecek.github.io/breakDown/"
	cran = "breakDown" 

	version("0.2.2", md5="ec1eb6e220149049d23d37d619f4ce14")
	version("0.2.1", md5="95b36145d88bba65f252710dc5167337")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
