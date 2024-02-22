# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpacetime(RPackage):
	"""Classes and Methods for Spatio-Temporal Data.

	Classes and methods for spatio-temporal data, including space-time regular
	lattices, sparse lattices, irregular data, and trajectories; utility
	functions for plotting data as map sequences (lattice or animation) or
	multiple time series; methods for spatial and temporal selection and
	subsetting, as well as for spatial/temporal/spatio-temporal matching or
	aggregation, retrieving coordinates, print, summary, etc."""

	cran = "spacetime"

	version("1.3-1", md5="cabe0b0e186f56a2cd3b7033b4c874ab")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-sp@1.1.0:", type=("build", "run"))
	depends_on("r-zoo@1.7.9:", type=("build", "run"))
	depends_on("r-xts@0.8.8:", type=("build", "run"))
	depends_on("r-intervals", type=("build", "run"))
