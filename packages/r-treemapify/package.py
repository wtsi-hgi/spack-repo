# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreemapify(RPackage):
	"""Draw Treemaps in 'ggplot2'

	Provides 'ggplot2' geoms for drawing treemaps.
	"""
	
	homepage = "https://wilkox.org/treemapify/"
	cran = "treemapify" 

	version("2.5.6", md5="847e38a1cf00dade72b7dc3c36a3f6be")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-ggfittext@0.5:", type=("build", "run"))
	depends_on("r-cli@3.6.1:", type=("build", "run"))
