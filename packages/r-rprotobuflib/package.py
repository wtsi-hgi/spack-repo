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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RProtoBufLib_2.14.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RProtoBufLib/RProtoBufLib_2.14.1.tar.gz"]

	version("2.20.0", tag="RELEASE_3_21")
	version("2.14.1", sha256="e26190b9058b49a44b0ec793990f185263737c6db68a73aee8aa462e2253be04")
	version("2.14.0", md5="e7351127e6b19daaae94fcecc970292b")

