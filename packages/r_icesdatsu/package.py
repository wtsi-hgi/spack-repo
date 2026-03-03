# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcesdatsu(RPackage):
	"""Functions to Interact with the ICES Data Submission Utility
(DATSU)

	Functions to Interact with the ICES Data Submission Utility (DATSU)
  <https://datsu.ices.dk/web/index.aspx>.
	"""
	
	homepage = "https://datsu.ices.dk/web/index.aspx"
	cran = "icesDatsu" 

	version("1.1.0", md5="4052dccfd673212260ec85a07066fd70")

	depends_on("r-icesconnect@1:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
