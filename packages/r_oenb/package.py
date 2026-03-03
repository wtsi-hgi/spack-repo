# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROenb(RPackage):
	"""Tools for the OeNB Data Web Service

	Tools to access data from the data web service of the Oesterreichische Nationalbank (OeNB), <https://www.oenb.at/en/Statistics/User-Defined-Tables/webservice.html>.
	"""
	
	homepage = "https://github.com/franzmohr/oenb"
	cran = "oenb" 

	version("0.0.2", md5="318c5d83f1417dc21f38db44ef96ebc8")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
