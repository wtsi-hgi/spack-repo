# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGhapps(RPackage):
	"""Authenticate as a 'GitHub' App

	'GitHub' apps provide a powerful way to manage fine grained
    programmatic access to specific 'git' repositories, without having to
    create dummy users, and which are safer than a personal access token
    for automated tasks. This package extends the 'gh' package to let you
    authenticate and interact with 'GitHub' <https://docs.github.com/en/rest/overview>
    in 'R' as an app.
	"""
	
	homepage = "https://github.com/r-lib/ghapps"
	cran = "ghapps" 

	version("1.0.0", md5="b6b64f08ba8e87f82b3fbff705a3c933")

	depends_on("r-gh", type=("build", "run"))
	depends_on("r-jose", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
