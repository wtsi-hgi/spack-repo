# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJjb(RPackage):
	"""Balamuta Miscellaneous

	Set of common functions used for manipulating colors,
    detecting and interacting with 'RStudio', modeling, formatting, determining
    users' operating system, feature scaling, and more!
	"""
	
	homepage = "https://github.com/coatless/jjb"
	cran = "jjb" 

	version("0.1.1", md5="0e5459ac4f16276824db3a062579acac")

