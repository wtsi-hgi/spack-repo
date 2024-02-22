# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPackcircles(RPackage):
	"""Circle Packing

	Algorithms to find arrangements of non-overlapping circles.
	"""
	
	homepage = "https://github.com/mbedward/packcircles"
	cran = "packcircles" 

	version("0.3.6", md5="a351da47abc0cb5e77c3bfd7ed103ea6")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcpp@1:", type=("build", "run"))
