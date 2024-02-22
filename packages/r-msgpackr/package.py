# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsgpackr(RPackage):
	"""A library to serialize or unserialize data in MessagePack format

	This is the library that can serialize or unserialize MessagePack format data.
	"""
	
	cran = "msgpackR" 

	version("1.1", md5="4c02160fe3f35499aa6e62e9003c4486")

