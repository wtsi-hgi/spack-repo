# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMakeunique(RPackage):
	"""Make Character Strings Unique

	Make all elements of a character vector unique. 
    Differs from 'make.unique' by starting at 1 and allowing users to customise suffix format.
	"""
	
	homepage = "https://github.com/selkamand/makeunique"
	cran = "makeunique" 

	version("1.0.0", md5="320935e3197127a8deb8859eb9e7fdaf")

