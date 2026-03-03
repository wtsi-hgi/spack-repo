# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDictionar6(RPackage):
	"""R6 Dictionary Interface

	Efficient object-oriented R6 dictionary capable of holding objects of any class, including R6. Typed and untyped dictionaries are provided as well as the 'usual' dictionary methods that are available in other OOP languages, for example listing keys, items, values, and methods to get/set these.
	"""
	
	homepage = "https://xoopR.github.io/dictionar6/"
	cran = "dictionar6" 

	version("0.1.3", md5="99f8f2228e3d4d26b640955a56d6547d", url="https://cran.r-project.org/src/contrib/dictionar6_0.1.3.tar.gz")

	depends_on("r-ooplah", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
