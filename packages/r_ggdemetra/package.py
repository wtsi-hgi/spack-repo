# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgdemetra(RPackage):
	"""'ggplot2' Extension for Seasonal and Trading Day Adjustment with
'RJDemetra'

	Provides 'ggplot2' functions to return the results of seasonal and trading day adjustment 
    made by 'RJDemetra'. 'RJDemetra' is an 'R' interface around 'JDemetra+' (<https://github.com/jdemetra/jdemetra-app>),
    the seasonal adjustment software officially recommended to the members of the European Statistical System and
    the European System of Central Banks.
	"""
	
	homepage = "https://aqlt.github.io/ggdemetra/"
	cran = "ggdemetra" 

	version("0.2.8", md5="690572c87a86ba6d4fa1e4f372abecd2")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-rjdemetra@0.1.2:", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("openjdk@8:", type=("build", "link", "run"))
