# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgplotMultistats(RPackage):
	"""Multiple Summary Statistics for Binned Stats/Geometries

	
    Provides the ggplot binning layer stat_summaries_hex(),
    which functions similar to its singular form,
    but allows the use of multiple statistics per bin.
    Those statistics can be mapped to multiple bin aesthetics.
	"""
	
	homepage = "https://github.com/flying-sheep/ggplot.multistats"
	cran = "ggplot.multistats" 

	version("1.0.0", md5="ec700c59f86395347b030d27a3e5b8b1")

	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-hexbin", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
