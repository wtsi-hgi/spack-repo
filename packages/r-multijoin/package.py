# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultijoin(RPackage):
	"""Enables Efficient Joining of Data File on Common Fields using
the Unix Utility Join

	Wrapper around the Unix join facility which is more efficient than the built-in R routine merge().
 The package enables the joining of multiple files on disk at once. 
 The files can be compressed and various filters can be deployed before joining.
 Compiles only under Unix.
	"""
	
	cran = "MultiJoin" 

	version("0.1.1", md5="65a97bd136bb582326aadd8ece050cf7")

	depends_on("r@2.10:", type=("build", "run"))
