# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWpp2015(RPackage):
	"""World Population Prospects 2015

	Provides data from the United Nation's World Population Prospects 2015.
	"""
	
	homepage = "http://esa.un.org/wpp"
	cran = "wpp2015" 

	version("1.1-2", md5="ed6ffbee428575a59526386f0445d400", url="https://cran.r-project.org/src/contrib/wpp2015_1.1-2.tar.gz")

	depends_on("r@2.14.2:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
