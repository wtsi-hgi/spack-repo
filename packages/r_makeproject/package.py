# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMakeproject(RPackage):
	"""Creates an empty package framework for the LCFD format

	This package creates an empty framework of files and
        directories for the "Load, Clean, Func, Do" structure described
        by Josh Reich.
	"""
	
	cran = "makeProject" 

	version("1.0", md5="2f88df5ef0ad114936f83c76e20414f8")

