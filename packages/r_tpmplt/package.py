# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTpmplt(RPackage):
	"""Tool-Kit for Dynamic Materials Model and Thermal Processing Maps

	Provides a simple approach for constructing dynamic materials
 modeling suggested by Prasad and Gegel (1984) <doi:10.1007/BF02664902>. It
 can easily generate various processing-maps based on this model as well. The
 calculation result in this package contains full materials constants, information
 about power dissipation efficiency factor, and rheological properties, can
 be exported completely also, through which further analysis and customized
 plots will be applicable as well.
	"""
	
	homepage = "https://github.com/CubicZebra/TPMplt"
	cran = "TPMplt" 

	version("0.1.4", md5="f71eedac0777aa67f0644599abb1373f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-vbtree", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-metr", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-dlm", type=("build", "run"))
