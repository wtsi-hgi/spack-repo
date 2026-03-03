# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAid(RPackage):
	"""Box-Cox Power Transformation

	Performs Box-Cox power transformation for different purposes, graphical approaches, assesses the success of the transformation via tests and plots, computes mean and confidence interval for back transformed data.
	"""
	
	cran = "AID" 

	version("2.9", md5="8ed1d1691853ed2fcb9d21a3404d687f")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-nortest", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-meta", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
