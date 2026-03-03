# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHttprequest(RPackage):
	"""Basic HTTP Request

	HTTP Request protocols. Implements the GET, POST and multipart POST request.
	"""
	
	cran = "httpRequest" 

	version("0.0.11", md5="1d6722c705238e53fa10918e3a2197d0")

