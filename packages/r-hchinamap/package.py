# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHchinamap(RPackage):
	"""Mapping China and Its Provinces

	By binding R functions and the 'Highmaps' <https://www.highcharts.com.cn/products/highmaps> chart library, 'hchinamap' package provides a simple way to map China and its provinces. The map of China drawn by this package contains complete Chinese territory, especially the Nine-dotted line, South Tibet, Hong Kong, Macao and Taiwan.
	"""
	
	homepage = "https://github.com/czxa/hchinamap"
	cran = "hchinamap" 

	version("0.1.0", md5="c29352cb22177fcede1e02fb46e69997")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
