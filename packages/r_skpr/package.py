# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSkpr(RPackage):
	"""Design of Experiments Suite: Generate and Evaluate Optimal
Designs

	Generates and evaluates D, I, A, Alias, E, T, and G optimal designs. Supports generation and evaluation of blocked and split/split-split/.../N-split plot designs. Includes parametric and Monte Carlo power evaluation functions, and supports calculating power for censored responses. Provides a framework to evaluate power using functions provided in other packages or written by the user. Includes a Shiny graphical user interface that displays the underlying code used to create and evaluate the design to improve ease-of-use and make analyses more reproducible. For details, see Morgan-Wall et al. (2021) <doi:10.18637/jss.v099.i01>.
	"""
	
	homepage = "https://github.com/tylermorganwall/skpr"
	cran = "skpr" 

	version("1.7.1", md5="05db1ce05a4ae36d695835be12a55d31")
	version("1.6.2", md5="5b13f68e2787c3c0d8230409c244562d")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-dofuture", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
