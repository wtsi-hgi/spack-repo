# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTilegramsr(RPackage):
	"""R Spatial Data for Tilegrams

	R spatial objects for Tilegrams.
  Tilegrams are tiled maps where the region size is proportional to
  the certain characteristics of the dataset.
	"""
	
	homepage = "https://github.com/bhaskarvk/tilegramsR"
	cran = "tilegramsR" 

	version("0.2.0", md5="e3a44267b7126d8ad306c87cc5d4b2f8")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
