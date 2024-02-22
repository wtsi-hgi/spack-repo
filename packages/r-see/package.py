# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSee(RPackage):
	"""Model Visualisation Toolbox for 'easystats' and 'ggplot2'

	Provides plotting utilities supporting packages in the 'easystats'
    ecosystem (<https://github.com/easystats/easystats>) and some extra themes,
    geoms, and scales for 'ggplot2'. Color scales are based on
    <https://materialui.co/colors>. 
    References: Lüdecke et al. (2021) <doi:10.21105/joss.03393>.
	"""
	
	homepage = "https://easystats.github.io/see/"
	cran = "see" 

	version("0.8.2", md5="708a39fe4312ec8d24664f6785e012a8")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-bayestestr@0.13.1:", type=("build", "run"))
	depends_on("r-correlation@0.8.4:", type=("build", "run"))
	depends_on("r-datawizard@0.9.1:", type=("build", "run"))
	depends_on("r-effectsize@0.8.6:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.4:", type=("build", "run"))
	depends_on("r-insight@0.19.8:", type=("build", "run"))
	depends_on("r-modelbased@0.8.6:", type=("build", "run"))
	depends_on("r-parameters@0.21.5:", type=("build", "run"))
	depends_on("r-performance@0.10.8:", type=("build", "run"))
