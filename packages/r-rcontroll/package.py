# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcontroll(RPackage):
	"""Individual-Based Forest Growth Simulator 'TROLL'

	'TROLL' is coded in C++ and it typically simulates hundreds of
    thousands of individuals over hundreds of years. The 'rcontroll' R package 
    is a wrapper of 'TROLL'. 'rcontroll' includes functions that generate inputs 
    for simulations and run simulations. Finally, it is possible to analyse 
    the 'TROLL' outputs through tables, figures, and maps taking advantage of 
    other R visualisation packages. 'rcontroll' also offers the possibility to 
    generate a virtual LiDAR point cloud that corresponds to a snapshot of 
    the simulated forest.
	"""
	
	homepage = "https://github.com/sylvainschmitt/rcontroll"
	cran = "rcontroll" 

	version("0.1.1", md5="e6bed0a8177e0f96168d7bdb1f6b1dde")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-readr@1.3:", type=("build", "run"))
	depends_on("r-sys@3.2:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-magrittr@2:", type=("build", "run"))
	depends_on("r-reshape2@1.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.2:", type=("build", "run"))
	depends_on("r-viridis@0.4:", type=("build", "run"))
	depends_on("r-doparallel@1.0.7:", type=("build", "run"))
	depends_on("r-dosnow@1.0.10:", type=("build", "run"))
	depends_on("r-foreach@1.4.1:", type=("build", "run"))
	depends_on("r-iterators@1.0.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-gganimate@1:", type=("build", "run"))
	depends_on("r-vroom@1:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-lubridate@1.6:", type=("build", "run"))
	depends_on("r-terra@1.5.16:", type=("build", "run"))
	depends_on("r-lidr@4.0.1:", type=("build", "run"))
	depends_on("r-rcppgsl", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
