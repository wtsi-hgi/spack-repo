# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAde4(RPackage):
	"""Analysis of Ecological Data : Exploratory and Euclidean Methods in
	Environmental Sciences.

	Tools for multivariate data analysis. Several methods are provided for the
	analysis (i.e., ordination) of one-table (e.g., principal component
	analysis, correspondence analysis), two-table (e.g., coinertia analysis,
	redundancy analysis), three-table (e.g., RLQ analysis) and K-table (e.g.,
	STATIS, multiple coinertia analysis). The philosophy of the package is
	described in Dray and Dufour (2007) <doi:10.18637/jss.v022.i04>."""

	cran = "ade4"

	license("GPL-2.0-or-later")

	version("1.7-22", md5="398ecb2bc76b202cd46fb9d3464f272b", url="https://cran.r-project.org/src/contrib/ade4_1.7-22.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pixmap", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
