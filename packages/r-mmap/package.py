# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmap(RPackage):
	"""Map Pages of Memory

	R interface to POSIX mmap and Window's MapViewOfFile.
	"""
	
	cran = "mmap" 

	version("0.6-22", md5="2c58501fd159e8a958239368f656cf7b")

