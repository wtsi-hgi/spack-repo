# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWpp2012(RPackage):
	"""World Population Prospects 2012

	Data from the United Nation's World Population Prospects 2012
	"""
	
	homepage = "http://esa.un.org/wpp"
	cran = "wpp2012" 

	version("2.2-1", md5="5089776935389cb9b80f9d79fdbeb61f", url="https://cran.r-project.org/src/contrib/wpp2012_2.2-1.tar.gz")

	depends_on("r@2.14.2:", type=("build", "run"))
