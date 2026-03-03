# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnmap(RPackage):
	"""China Map Data from AutoNavi Map

	According to the code or the name of the administrative division at the county level and above provided by the Ministry of Civil Affairs of the People's Republic of China in 2022 (<https://www.mca.gov.cn/mzsj/xzqh/2022/202201xzqh.html>), get the map file online from the website of AutoNavi Map (<http://datav.aliyun.com/portal/school/atlas/area_selector>).
	"""
	
	homepage = "https://github.com/PanfengZhang/cnmap"
	cran = "cnmap" 

	version("0.1.0", md5="c780820a2460f00e870307bbe694c548")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
