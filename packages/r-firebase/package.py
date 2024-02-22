# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFirebase(RPackage):
	"""Integrates 'Google Firebase' Authentication Storage, and
'Analytics' with 'Shiny'

	Authenticate users in 'Shiny' applications using 'Google Firebase'
    with any of the many methods provided; email and password, email link, or
    using a third-party provider such as 'Github', 'Twitter', or 'Google'.
    Use 'Firebase Storage' to store files securely, and leverage 'Firebase Analytics'
    to easily log events and better understand your audience.
	"""
	
	homepage = "https://firebase.john-coene.com/"
	cran = "firebase" 

	version("1.0.2", md5="f7c504a68b25c4da9a90f1b8db186f6c")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-jose", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
