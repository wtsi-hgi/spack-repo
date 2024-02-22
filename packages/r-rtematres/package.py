# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtematres(RPackage):
	"""The rtematres API package

	Exploit controlled vocabularies organized on tematres servers.
	"""
	
	homepage = "https://github.com/cpfaff/rtematres"
	cran = "rtematres" 

	version("0.2", md5="10fb8e1663afaf32b5919b12135fc7e4")

	depends_on("r-xml", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-gdata", type=("build", "run"))
