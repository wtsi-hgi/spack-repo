# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScuttle(RPackage):
	"""Single-Cell RNA-Seq Analysis Utilities.

	Provides basic utility functions for performing single-cell analyses,
	focusing on simple normalization, quality control and data transformations.
	Also provides some helper functions to assist development of other
	packages."""

	bioc = "scuttle"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/scuttle_1.12.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/scuttle/scuttle_1.12.0.tar.gz"]

	version("1.12.0", md5="b784ac30ef76b7c0cdac8b79be67b995")

	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-delayedmatrixstats", type=("build", "run"))
	depends_on("r-beachmat", type=("build", "run"))
