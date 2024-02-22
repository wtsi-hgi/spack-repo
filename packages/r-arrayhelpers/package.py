# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArrayhelpers(RPackage):
	"""Convenience Functions for Arrays

	Some convenient functions to work with arrays.
	"""
	
	homepage = "http://arrayhelpers.r-forge.r-project.org/"
	cran = "arrayhelpers" 

	version("1.1-0", md5="d94d13f45d5f4c8a771c1c670a5368e6")

	depends_on("r-svunit", type=("build", "run"))
