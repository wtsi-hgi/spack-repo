# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdestr(RPackage):
	"""Estimation in Optimal Adaptive Two-Stage Designs

	
  Methods to evaluate the performance characteristics of
  various point and interval estimators for optimal adaptive two-stage designs.
  Specifically, this package is written to work with trial designs created by the 'adoptr' package
  (Kunzmann et al. (2021) <doi:10.18637/jss.v098.i09>; Pilz et al. (2021) <doi:10.1002/sim.8953>)).
  Apart from the a priori evaluation of performance characteristics, this package also allows for the
  evaluation of the implemented estimators on real datasets, and it implements methods
  to calculate p-values.
	"""
	
	homepage = "https://jan-imbi.github.io/adestr/"
	cran = "adestr" 

	version("0.5.0", md5="5c28f7c3d2c490dfbdb8e1a0d24fe11d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-latex2exp", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
