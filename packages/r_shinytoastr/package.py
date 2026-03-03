# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinytoastr(RPackage):
	"""Notifications from 'Shiny'

	Browser notifications in 'Shiny' apps, using
    'toastr': <https://github.com/CodeSeven/toastr#readme>.
	"""
	
	homepage = "https://github.com/gaborcsardi/shinytoastr"
	cran = "shinytoastr" 

	version("2.2.0", md5="e4c0f129bd9ce5e7b3b2677bda2b2a62")

	depends_on("r-shiny", type=("build", "run"))
