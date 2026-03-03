# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAcdm(RPackage):
	"""Tools for Autoregressive Conditional Duration Models

	Package for Autoregressive Conditional Duration (ACD, Engle and Russell, 1998) models. Creates trade, price or volume durations from transactions (tic) data, performs diurnal adjustments, fits various ACD models and tests them. 
	"""
	
	cran = "ACDm" 

	version("1.0.4.3", md5="0d69296d1044cc03c308879e3f63dbd5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
