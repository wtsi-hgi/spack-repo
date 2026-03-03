# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPanelwranglr(RPackage):
	"""Panel Data Wrangling Tools

	Leading/lagging a panel, creating dummy variables,
             taking panel differences, looking for panel autocorrelations,
             and more. Implemented via a 'data.table' back end. 
	"""
	
	homepage = "https://github.com/JSzitas/panelWranglR"
	cran = "panelWranglR" 

	version("1.2.13", md5="bdf7c3b47f14af06bb384f21af0427bb")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
