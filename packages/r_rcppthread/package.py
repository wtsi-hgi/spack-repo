# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppthread(RPackage):
	"""R-Friendly Threading in C++

	Provides a C++11-style thread class and thread pool that can safely
    be interrupted from R. See Nagler (2021) <doi:10.18637/jss.v097.c01>.
	"""
	
	homepage = "https://github.com/tnagler/RcppThread"
	cran = "RcppThread" 

	version("2.1.7", md5="846c28d124e57d8158112db1ab59a909")

	depends_on("r@3.3:", type=("build", "run"))
