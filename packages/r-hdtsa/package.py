# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdtsa(RPackage):
	"""High Dimensional Time Series Analysis Tools

	Procedures for high-dimensional time series analysis including factor analysis proposed by Lam and Yao (2012) <doi:10.1214/12-AOS970> and Chang, Guo and Yao (2015) <doi:10.1016/j.jeconom.2015.03.024>, martingale difference test proposed by Chang, Jiang and Shao (2021) preprint, principal component analysis proposed by Chang, Guo and Yao (2018) <doi:10.1214/17-AOS1613>, identifying conintegration proposed by Zhang, Robinson and Yao (2019) <doi:10.1080/01621459.2018.1458620>, unit root test proposed by Chang, Cheng and Yao (2021) <doi:10.1093/biomet/asab034> and white noise test proposed by Chang, Yao and Zhou (2017) <doi:10.1093/biomet/asw066>.
	"""
	
	homepage = "https://github.com/Linc2021/HDTSA"
	cran = "HDTSA" 

	version("1.0.2", md5="f8d8641365ff533c78730beff7d06c4a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-clime", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
