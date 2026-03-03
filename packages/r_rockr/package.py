# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRockr(RPackage):
	"""'Rock' R Server Client

	Connector to the REST API of a 'Rock' R server, to perform operations 
  on a remote R server session, or administration tasks. See 'Rock' documentation at
  <https://rockdoc.obiba.org/>.
	"""
	
	cran = "rockr" 

	version("1.0.0", md5="804b01ce7c0874c7be1376a0a36b8abf")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-mime", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
