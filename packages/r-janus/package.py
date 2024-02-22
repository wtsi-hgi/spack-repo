# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJanus(RPackage):
	"""Optimized Recommending System Based on 'tensorflow'

	Proposes a coarse-to-fine optimization of a recommending system based on deep-neural networks using 'tensorflow'.
	"""
	
	homepage = "https://rpubs.com/giancarlo_vercellino/janus"
	cran = "janus" 

	version("1.0.0", md5="88db00a5258af1d30e7aa04fec4433fe")

	depends_on("r-keras@2.9:", type=("build", "run"))
	depends_on("r-tensorflow@2.9:", type=("build", "run"))
	depends_on("r-dplyr@1.0.10:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-forcats@0.5.1:", type=("build", "run"))
	depends_on("r-tictoc@1.0.1:", type=("build", "run"))
	depends_on("r-readr@2.1.2:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.6:", type=("build", "run"))
	depends_on("r-narray@0.4.1.1:", type=("build", "run"))
	depends_on("r-lubridate@1.7.10:", type=("build", "run"))
	depends_on("r-rcppalgos@2.6:", type=("build", "run"))
	depends_on("r-rmpfr@0.8.7:", type=("build", "run"))
	depends_on("r-metrics@0.1.4:", type=("build", "run"))
	depends_on("r-statrank@0.0.6:", type=("build", "run"))
	depends_on("r-hash@2.2.6.2:", type=("build", "run"))
	depends_on("r-reticulate@1.26:", type=("build", "run"))
