# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInfotheo(RPackage):
	"""Information-Theoretic Measures

	Implements various measures of information theory based on several entropy estimators.
	"""
	
	homepage = "http://homepage.meyerp.com/software"
	cran = "infotheo" 

	version("1.2.0.1", md5="980ad0bc179733e870c25276cc95680e")

