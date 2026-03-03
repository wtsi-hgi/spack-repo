# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWpp2017(RPackage):
	"""World Population Prospects 2017

	Provides data from the United Nation's World Population Prospects 2017.
	"""
	
	homepage = "http://population.un.org/wpp"
	cran = "wpp2017" 

	version("1.2-3", md5="8ff291699cf2dff09fb3b5c68ff4318a", url="https://cran.r-project.org/src/contrib/wpp2017_1.2-3.tar.gz")

	depends_on("r@2.14.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
