# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFcps(RPackage):
	"""Fundamental Clustering Problems Suite

	Over sixty clustering algorithms are provided in this package with consistent input and output, which enables the user to try out algorithms swiftly. Additionally, 26 statistical approaches for the estimation of the number of clusters as well as the mirrored density plot (MD-plot) of clusterability are implemented. The packages is published in Thrun, M.C., Stier Q.: "Fundamental Clustering Algorithms Suite" (2021), SoftwareX, <DOI:10.1016/j.softx.2020.100642>. Moreover, the fundamental clustering problems suite (FCPS) offers a variety of clustering challenges any algorithm should handle when facing real world data, see Thrun, M.C., Ultsch A.: "Clustering Benchmark Datasets Exploiting the Fundamental Clustering Problems" (2020), Data in Brief, <DOI:10.1016/j.dib.2020.105501>.
	"""
	
	homepage = "https://www.deepbionics.org/"
	cran = "FCPS" 

	version("1.3.4", md5="749ba6fd6322916b39cfcbc8843280a8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-datavisualizations", type=("build", "run"))
	depends_on("pandoc@1.12.3:", type=("build", "link", "run"))
