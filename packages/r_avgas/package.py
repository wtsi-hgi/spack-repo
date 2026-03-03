# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAvgas(RPackage):
	"""A Variable Selection using Genetic Algorithms

	We provide a stage-wise selection method using genetic algorithm which can perform fast interaction selection in high-dimensional linear regression models with two-way interaction effects under strong, weak, or no heredity condition. Ye, C.,and Yang,Y. (2019) <doi:10.1109/TIT.2019.2913417>.
	"""
	
	cran = "AVGAS" 

	version("0.1.0", md5="68b477883203c08c58db8333452ac494")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-selectiveinference", type=("build", "run"))
	depends_on("r-variablescreening", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
