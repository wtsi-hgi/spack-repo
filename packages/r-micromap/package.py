# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicromap(RPackage):
	"""Linked Micromap Plots

	This group of functions simplifies the creation of linked micromap plots. Please
  see <https://www.jstatsoft.org/v63/i02/> for additional details.
	"""
	
	homepage = "<https://github.com/fawda123/micromap>"
	cran = "micromap" 

	version("1.9.8", md5="42d5b7e97e5089f8d256c33f1e197f83")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
