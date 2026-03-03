# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvalues(RPackage):
	"""Measures of the Sturdiness of Regression Coefficients

	Implements the s-values proposed by Ed. Leamer.
    It provides a context-minimal approach for sensitivity analysis using extreme
    bounds to assess the sturdiness of regression coefficients.
	"""
	
	cran = "sValues" 

	version("0.1.6", md5="49357476e9de5301251b01ab92fdff32")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
