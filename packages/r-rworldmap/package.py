# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRworldmap(RPackage):
	"""Mapping Global Data

	Enables mapping of country level and gridded user datasets.
	"""
	
	homepage = "https://github.com/AndySouth/rworldmap/"
	cran = "rworldmap" 

	version("1.3-8", md5="c9c1708704266d4671fe5ec00a8aa0dd")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
