# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLgrextra(RPackage):
	"""Extra Appenders for 'lgr'

	Additional appenders for the logging package 'lgr' that
    support logging to databases, email and push notifications.
	"""
	
	cran = "lgrExtra" 

	version("0.0.8", md5="7a79e8a8782d47235466acc2f73a990d")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-lgr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
