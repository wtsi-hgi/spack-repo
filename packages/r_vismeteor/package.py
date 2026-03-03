# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVismeteor(RPackage):
	"""Analysis of Visual Meteor Data

	Provides a suite of analytical functionalities to process and analyze
    visual meteor observations from the Visual Meteor Database
    of the International Meteor Organization <https://www.imo.net/>.
	"""
	
	homepage = "https://github.com/jankorichter/vismeteor"
	cran = "vismeteor" 

	version("1.8.5", md5="f39f0513e3d274976f8b84a28d691c0d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
