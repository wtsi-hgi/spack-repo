# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWpp2019(RPackage):
	"""World Population Prospects 2019

	Provides data from the United Nation's World Population Prospects 2019.
	"""
	
	homepage = "http://population.un.org/wpp"
	cran = "wpp2019" 

	version("1.1-1", md5="09a296fc98b69f2fbc2fc920415c9891", url="https://cran.r-project.org/src/contrib/wpp2019_1.1-1.tar.gz")

	depends_on("r@2.14.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
