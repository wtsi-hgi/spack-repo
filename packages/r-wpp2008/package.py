# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWpp2008(RPackage):
	"""World Population Prospects 2008

	Data from the United Nation's World Population Prospects 2008
	"""
	
	homepage = "http://esa.un.org/wpp/index.htm"
	cran = "wpp2008" 

	version("1.0-1", md5="fec95a11b631bcbe80ec227eb1af05c2", url="https://cran.r-project.org/src/contrib/wpp2008_1.0-1.tar.gz")

	depends_on("r@2.14.2:", type=("build", "run"))
