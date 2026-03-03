# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsadbe(RPackage):
	"""Data related to the book "R Statistical Application Development
by Example"

	The package contains all the data sets related to the book
        written by the maintainer of the package.
	"""
	
	cran = "RSADBE" 

	version("1.0", md5="7995e46d06ecd2b48eb0ff242a886e02")

