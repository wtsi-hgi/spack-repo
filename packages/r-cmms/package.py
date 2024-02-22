# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmms(RPackage):
	"""Compositional Mediation Model

	A compositional mediation model for continuous outcome and binary outcomes to deal with mediators that are compositional data. Lin, Ziqiang et al. (2022) <doi:10.1016/j.jad.2021.12.019>.
	"""
	
	cran = "CMMs" 

	version("1.0.0", md5="c57992beaf5ca674436f0d46e7d7312b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fastdummies", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-robcompositions", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
