# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdian(RPackage):
	"""Client Library for The Guardian

	A client library for 'The Guardian' (https://www.guardian.com/)
    and their API, this package allows users to search for Guardian articles and
    retrieve both the content and metadata.
	"""
	
	homepage = "https://github.com/ironholds/rdian"
	cran = "rdian" 

	version("0.1.1", md5="c90955dacde66743b5d2b77e45d2e753")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
