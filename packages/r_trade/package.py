# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrade(RPackage):
	"""Tools for Trade Practitioners

	A collection of tools for trade practitioners, including the ability to calibrate different consumer demand systems and simulate the effects of tariffs and quotas under different competitive regimes. These tools are derived from Anderson et al. (2001) <doi:10.1016/S0047-2727(00)00085-2> and Froeb et al. (2003) <doi:10.1016/S0304-4076(02)00166-5>.
	"""
	
	homepage = "https://github.com/luciu5/trade"
	cran = "trade" 

	version("0.8.1", md5="38d14cd943c0656ecbcbfeb9f2401524")

	depends_on("r-antitrust@0.99.11:", type=("build", "run"))
