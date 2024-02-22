# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFormshare(RPackage):
	"""A Simple Connection Between the 'FormShare App' and 'R' for
Advanced Analytics

	Provides analytics directly from 'R'. It requires:
    'FormShare App': <https://github.com/qlands/FormShare >= 2.22.0> .
    Analytics plugin: <https://github.com/qlands/formshare_analytics_plugin> .
    Remote SQL plugin: <https://github.com/qlands/formshare_sql_plugin> .
	"""
	
	homepage = "https://github.com/qlands/formshare-R-package"
	cran = "FormShare" 

	version("1.0.1", md5="c143f047062ae8eee6a141e0ffca9771")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
