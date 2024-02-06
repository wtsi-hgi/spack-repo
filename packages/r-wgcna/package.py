# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWgcna(RPackage):
	"""Weighted Correlation Network Analysis.

	Functions necessary to perform Weighted Correlation Network Analysis on
	high-dimensional data as originally described in Horvath and Zhang (2005)
	<doi:10.2202/1544-6115.1128> and Langfelder and Horvath (2008)
	<doi:10.1186/1471-2105-9-559>. Includes functions for rudimentary data
	cleaning, construction of correlation networks, module identification,
	summarization, and relating of variables and modules to sample traits. Also
	includes a number of utility functions for data manipulation and
	visualization."""

	cran = "WGCNA"

	version("1.72-5", md5="15c7021e172261124fe0e20aefdabbe9")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-dynamictreecut@1.62:", type=("build", "run"))
	depends_on("r-fastcluster", type=("build", "run"))
	depends_on("r-matrixstats@0.8.1:", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
