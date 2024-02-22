# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKosis(RPackage):
	"""Korean Statistical Information Service (KOSIS)

	API wrapper to download statistical information from the
             Korean Statistical Information Service (KOSIS)
             <https://kosis.kr/openapi/index/index.jsp>.
	"""
	
	cran = "kosis" 

	version("0.0.1", md5="c94a57b71db143699e1d53d90200b72a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table@1.13:", type=("build", "run"))
	depends_on("r-httr@1.4.3:", type=("build", "run"))
	depends_on("r-jsonlite@1.7.2:", type=("build", "run"))
	depends_on("r-tibble@3.2.1:", type=("build", "run"))
