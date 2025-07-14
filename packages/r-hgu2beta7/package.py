# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu2beta7(RPackage):
	"""A data package containing annotation data for hgu2beta7

	Annotation data file for hgu2beta7 assembled using data from public data repositories
	"""
	
	bioc = "hgu2beta7"

	version("1.48.0", commit="7525d2410fe379c5fad89e6c1619d8dd4a416772")
	version("1.42.0", commit="04e83dd3985a5cc7244fc88c6ab47a3138e00439")

	depends_on("r@2:", type=("build", "run"))

