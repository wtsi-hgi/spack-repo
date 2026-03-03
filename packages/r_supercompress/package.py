# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSupercompress(RPackage):
	"""Supervised Compression of Big Data

	A supervised compression method that incorporates the response for reducing big data to a carefully selected subset. Please see Joseph and Mak (2021) <doi:10.1002/sam.11508>. This research is supported by a U.S. National Science Foundation (NSF) grant CMMI-1921646.
	"""
	
	cran = "supercompress" 

	version("1.1", md5="912731254f38cf6983fd413bbcdb81ee")

	depends_on("r-fnn", type=("build", "run"))
