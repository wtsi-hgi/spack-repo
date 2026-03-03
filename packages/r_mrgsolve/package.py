# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrgsolve(RPackage):
	"""Simulate from ODE-Based Models

	Fast simulation from ordinary differential equation
    (ODE) based models typically employed in quantitative pharmacology and
    systems biology.
	"""
	
	homepage = "https://github.com/metrumresearchgroup/mrgsolve"
	cran = "mrgsolve" 

	version("1.4.1", md5="68005b07bd273e24d1f671a9da1735f0")

	depends_on("r@3.6.2:", type=("build", "run"))
	depends_on("r-rcpp@1.0.7:", type=("build", "run"))
	depends_on("r-dplyr@1.0.8:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
	depends_on("r-tibble@3.1.6:", type=("build", "run"))
	depends_on("r-rlang@1.0.1:", type=("build", "run"))
	depends_on("r-tidyselect@1.1.1:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.10.7.3:", type=("build", "run"))
	depends_on("r-bh@1.75.0.0:", type=("build", "run"))
