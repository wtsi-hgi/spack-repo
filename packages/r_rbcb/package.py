# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbcb(RPackage):
	"""R Interface to Brazilian Central Bank Web Services

	The Brazilian Central Bank API delivers many datasets which regard economic
  activity, regional economy, international economy, public finances, credit
  indicators and many more. For more information please see <http://dadosabertos.bcb.gov.br/>.
  These datasets can be accessed through 'rbcb' functions and can be obtained in
  different data structures common to R ('tibble', 'data.frame', 'xts', ...).
	"""
	
	homepage = "https://github.com/wilsonfreitas/rbcb"
	cran = "rbcb" 

	version("0.1.14", md5="bfb903947c1636d9a2fb206c20b83d39")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
