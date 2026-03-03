# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGetlattesdata(RPackage):
	"""Reading Bibliometric Data from Lattes Platform

	A simple API for downloading and reading xml data directly from Lattes <http://lattes.cnpq.br/>.
	"""
	
	homepage = "https://github.com/msperlin/GetLattesData/"
	cran = "GetLattesData" 

	version("1.4.3", md5="5f9d92f1ebea27e197e9474f73d16de6")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
