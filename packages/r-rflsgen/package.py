# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRflsgen(RPackage):
	"""Neutral Landscape Generator with Targets on Landscape Indices

	Interface to the 'flsgen' neutral landscape generator <https://github.com/dimitri-justeau/flsgen>. It allows to
  - Generate fractal terrain;
  - Generate landscape structures satisfying user targets over landscape indices;
  - Generate landscape raster from landscape structures.
	"""
	
	homepage = "https://dimitri-justeau.github.io/rflsgen/"
	cran = "rflsgen" 

	version("1.2.1", md5="4f7fce0e11f09b54ac498ed5e21b3378")

	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-terra@1.5.12:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("openjdk@8:", type=("build", "link", "run"))
