# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYacca(RPackage):
	"""Yet Another Canonical Correlation Analysis Package

	An alternative canonical correlation/redundancy analysis function, with associated print, plot, and summary methods.  A method for generating helio plots is also included.
	"""
	
	cran = "yacca" 

	version("1.4-2", md5="77c3433cacbaaf8cccfdaf7478226d91")

	depends_on("r@1.8:", type=("build", "run"))
