# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCliapp(RPackage):
	"""Create Rich Command Line Applications

	Create rich command line applications, with colors, headings,
    lists, alerts, progress bars, etc. It uses CSS for custom themes.
	"""
	
	homepage = "https://github.com/r-lib/cliapp#readme"
	cran = "cliapp" 

	version("0.1.1", md5="9658b6f6d77fee78100b4cee6b5b5616")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-fansi", type=("build", "run"))
	depends_on("r-glue@1.3:", type=("build", "run"))
	depends_on("r-prettycode", type=("build", "run"))
	depends_on("r-progress@1.2:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-selectr", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
