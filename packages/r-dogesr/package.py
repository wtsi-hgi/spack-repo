# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDogesr(RPackage):
	"""Work with the Doges/Dogaresse Dataset

	Work with data on Venetian doges and dogaresse and the noble families of the Republic of Venice, and use it for social network analysis, as used in Merelo (2022) <arXiv:2209.07334>.
	"""
	
	cran = "dogesr" 

	version("0.5.0", md5="c35b9a73bf5789cb4bec4372831cf805")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-qpdf", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
