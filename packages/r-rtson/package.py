# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtson(RPackage):
	"""Typed JSON

	TSON, short for Typed JSON, is a binary-encoded serialization of
    JSON like document that support JavaScript typed data (https://github.com/tercen/TSON).
	"""
	
	homepage = "https://github.com/tercen/TSON"
	cran = "rtson" 

	version("1.3", md5="9cea864bfb40cf8b5818755dc36e6853")

	depends_on("r-r6", type=("build", "run"))
