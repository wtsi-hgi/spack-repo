# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGggenes(RPackage):
	"""Draw Gene Arrow Maps in 'ggplot2'

	A 'ggplot2' extension for drawing gene arrow maps.
	"""
	
	homepage = "https://wilkox.org/gggenes/"
	cran = "gggenes" 

	version("0.5.1", md5="4d0a9493eca86eeac48fb62b472e5879")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-ggfittext@0.8:", type=("build", "run"))
	depends_on("r-rlang@0.2:", type=("build", "run"))
