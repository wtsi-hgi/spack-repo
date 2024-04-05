# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGdatools(RPackage):
	"""Geometric Data Analysis

	Many tools for Geometric Data Analysis (Le Roux & Rouanet (2005) <doi:10.1007/1-4020-2236-0>), such as MCA variants (Specific Multiple Correspondence Analysis, Class Specific Analysis), many graphical and statistical aids to interpretation (structuring factors, concentration ellipses, inductive tests, bootstrap validation, etc.) and multiple-table analysis (Multiple Factor Analysis, between- and inter-class analysis, Principal Component Analysis and Correspondence Analysis with Instrumental Variables, etc.).
	"""
	
	homepage = "https://github.com/nicolas-robette/GDAtools"
	cran = "GDAtools" 

	version("2.1", md5="fe4ec38d17884eb93d3d1e3b3e7eda3b")
	version("2.0.1", md5="7a7d785ac69524a43ef76335542c9ec2")

	depends_on("r-descriptio@1.2:", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
