# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMb(RPackage):
	"""The Use of Marginal Distributions in Conditional Forecasting

	A new way to predict time series using the marginal distribution table in the absence of the significance of traditional models.
	"""
	
	cran = "MB" 

	version("0.1.1", md5="bf1c8cd951e226e69dbc67c41b81e0ae")

	depends_on("r-tibble", type=("build", "run"))
