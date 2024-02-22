# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRscontract(RPackage):
	"""Generic implementation of the 'RStudio' connections contract

	Provides a generic implementation of the 'RStudio' connection contract to 
    make it easier for database connections, and other type of connections, opened 
    via R packages integrate with the connections pane inside the 'RStudio' interactive
    development environment (IDE).
	"""
	
	homepage = "https://github.com/rstudio/rscontract"
	cran = "rscontract" 

	version("0.1.2", md5="34be70ffb559b71dabe91915ab706368")

