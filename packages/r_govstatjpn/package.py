# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGovstatjpn(RPackage):
	"""functions to get public survey data in Japan

	This package purposes to deal with public survey data of
        Japanese government via their Application Programming Interface
        (http://statdb.nstac.go.jp/)
	"""
	
	cran = "govStatJPN" 

	version("0.1", md5="2418c2a05c93a6471f478616f63bc8fd")

