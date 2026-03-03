# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoauth(RPackage):
	"""R Interface For OAuth

	Provides an interface to the OAuth 1.0 specification
        allowing users to authenticate via OAuth to the
        server of their choice.
	"""
	
	cran = "ROAuth" 

	version("0.9.6", md5="00107bc883851505590a4dce6cdf2142")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
