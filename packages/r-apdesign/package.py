# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApdesign(RPackage):
	"""An Implementation of the Additive Polynomial Design Matrix

	An implementation of the additive polynomial (AP) design matrix. It
    constructs and appends an AP design matrix to a data frame for use with
    longitudinal data subject to seasonality.
	"""
	
	cran = "apdesign" 

	version("1.0.0", md5="0639f2a1c05fddf45229e18c5b4fc39e")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-matrix@1.2:", type=("build", "run"))
