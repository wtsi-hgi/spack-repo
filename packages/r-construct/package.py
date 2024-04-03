# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConstruct(RPackage):
	"""Models Spatially Continuous and Discrete Population GeneticStructure.

	A method for modeling genetic data as a combination of discrete layers,
	within each of which relatedness may decay continuously with geographic
	distance. This package contains code for running analyses (which are
	implemented in the modeling language 'rstan') and visualizing and
	interpreting output. See the paper for more details on the model and its
	utility."""

	cran = "conStruct"
	version("1.0.5", sha256="4d953073bd1f374a91655b4889ab1b65d92a1c89ea39eb3dac5cd852a42b8a7c")
	version("1.0.4", sha256="4e585b718a361061bc1432cea46fc65f802fb0ef58e4516d33e1af99bbfe90ce")
	version("1.0.3", sha256="b449c133a944ad05a28f84f312ed4ccbc1574c4659aa09c678618d2ae9008310")
	version("1.0.6", md5="3b3ee2f8083c0978303256730f74c734")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@1.5:", type=("build", "run"))
	depends_on("r-caroline", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
