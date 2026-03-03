# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPanelhetero(RPackage):
	"""Panel Data Analysis with Heterogeneous Dynamics

	Understanding the dynamics of potentially heterogeneous variables is important in statistical applications.
    This package provides tools for estimating the degree of heterogeneity across cross-sectional units in the panel data analysis.
    The methods are developed by Okui and Yanagi (2019) <doi:10.1016/j.jeconom.2019.04.036> and Okui and Yanagi (2020) <doi:10.1093/ectj/utz019>.
	"""
	
	homepage = "https://tkhdyanagi.github.io/panelhetero/"
	cran = "panelhetero" 

	version("1.0.1", md5="4f8c847b935ee2137d72bff7ed0e399f")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-rearrangement", type=("build", "run"))
