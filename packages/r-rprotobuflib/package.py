# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRprotobuflib(RPackage):
	"""C++ headers and static libraries of Protocol buffers

	This package provides the headers and static library of Protocol buffers for other R packages to compile and link against.
	"""
	
	bioc = "RProtoBufLib"

	version("2.20.0", commit="df750e3a21f1cd45b840fd3b263b88fc16c0f59b")
	version("2.14.1", commit="cb81f5637e763f4ffe8b11a76548f5935afef5bd")
	version("2.14.0", md5="e7351127e6b19daaae94fcecc970292b")

