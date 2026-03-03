# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNhsrplotthedots(RPackage):
	"""Draw XmR Charts for NHSE/I 'Making Data Count' Programme

	Provides tools for drawing Statistical Process Control (SPC) charts. This package supports the NHSE/I
  programme 'Making Data Count', and allows users to draw XmR charts, use change points and apply rules with summary
  indicators for when rules are breached.
	"""
	
	homepage = "https://nhs-r-community.github.io/NHSRplotthedots/"
	cran = "NHSRplotthedots" 

	version("0.1.0", md5="6fcad41fddcbb603ddb11b9e050e0197")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-nhsrdatasets", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
