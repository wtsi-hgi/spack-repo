# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcos(RPackage):
	"""Economic Statistics System of the Bank of Korea

	API wrapper to download statistical information from the Economic
             Statistics System (ECOS) of the Bank of Korea
             <https://ecos.bok.or.kr/api/#/>.
	"""
	
	cran = "ecos" 

	version("0.1.6", md5="5173aa55ae09658c79c91d8c590b36e2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr@1.4.3:", type=("build", "run"))
	depends_on("r-jsonlite@1.7.2:", type=("build", "run"))
	depends_on("r-xml@3.99:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
