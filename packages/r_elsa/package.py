# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElsa(RPackage):
	"""Entropy-Based Local Indicator of Spatial Association

	A framework that provides the methods for quantifying entropy-based local indicator of spatial association (ELSA) that can be used for both continuous and categorical data. In addition, this package offers other methods to measure local indicators of spatial associations (LISA). Furthermore, global spatial structure can be measured using a variogram-like diagram, called entrogram. For more information, please check that paper: Naimi, B., Hamm, N. A., Groen, T. A., Skidmore, A. K., Toxopeus, A. G., & Alibakhshi, S. (2019) <doi:10.1016/j.spasta.2018.10.001>.
	"""
	
	homepage = "http://r-gis.net"
	cran = "elsa" 

	version("1.1-28", md5="f32f570cc050f0fa1eb04a8b223db77a")

	depends_on("r-sp@1.2.0:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r@3:", type=("build", "run"))
