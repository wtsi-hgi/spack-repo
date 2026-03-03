# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLanguagelayer(RPackage):
	"""Access the 'languagelayer' API

	Improve your text analysis with languagelayer
        <https://languagelayer.com>, a powerful language detection
        API.
	"""
	
	homepage = "https://github.com/ColinFay/languagelayer"
	cran = "languagelayeR" 

	version("1.2.4", md5="9ff86e1300a429beca46cff4efc3c110")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-attempt", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
