# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgsurvfit(RPackage):
	"""Flexible Time-to-Event Figures

	Ease the creation of time-to-event (i.e. survival) endpoint
    figures. The modular functions create figures ready for publication.
    Each of the functions that add to or modify the figure are written as
    proper 'ggplot2' geoms or stat methods, allowing the functions from
    this package to be combined with any function or customization from
    'ggplot2' and other 'ggplot2' extension packages.
	"""
	
	homepage = "https://github.com/pharmaverse/ggsurvfit"
	cran = "ggsurvfit" 

	version("1.0.0", md5="8a1099f843856b1784fe69cf8a1deaf3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-broom@1:", type=("build", "run"))
	depends_on("r-cli@3:", type=("build", "run"))
	depends_on("r-dplyr@1.0.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-glue@1.6:", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-patchwork@1.1:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-survival@3.4.0:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
