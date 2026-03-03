# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaptiles(RPackage):
	"""Download and Display Map Tiles

	To create maps from tiles, 'maptiles' downloads, composes and
    displays tiles from a large number of providers (e.g. 'OpenStreetMap',
    'Stadia', 'Esri', 'CARTO', or 'Thunderforest').
	"""
	
	homepage = "https://github.com/riatelab/maptiles/"
	cran = "maptiles" 

	version("0.7.0", md5="5f54895b40f6dc327bad1e36a986af65")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sf@0.9.5:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-slippymath", type=("build", "run"))
