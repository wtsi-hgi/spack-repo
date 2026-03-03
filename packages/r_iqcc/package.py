# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIqcc(RPackage):
	"""Improved Quality Control Charts

	Builds statistical control charts with exact limits for
        univariate and multivariate cases.
	"""
	
	homepage = "https://flaviobarros.github.io/IQCC"
	cran = "IQCC" 

	version("0.7", md5="b8a57dc12fa437a5dc82cdba73c866a6")

	depends_on("r@3.4.2:", type=("build", "run"))
	depends_on("r-misctools", type=("build", "run"))
	depends_on("r-qcc", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
