# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWpp2010(RPackage):
	"""World Population Prospects 2010

	Data from the United Nation's World Population Prospects
        2010
	"""
	
	homepage = "http://esa.un.org/wpp"
	cran = "wpp2010" 

	version("1.2-0", md5="15185a8b7deaddbdcc5861bff1cc6587", url="https://cran.r-project.org/src/contrib/wpp2010_1.2-0.tar.gz")

	depends_on("r@2.14.2:", type=("build", "run"))
