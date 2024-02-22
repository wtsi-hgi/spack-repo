# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRequire(RPackage):
	"""Installing and Loading R Packages for Reproducible Workflows.

	A single key function, 'Require' that wraps 'install.packages',
	'remotes::install_github', 'versions::install.versions', and
	'base::require' that allows for reproducible workflows. As with other
	functions in a reproducible workflow, this package emphasizes functions
	that return the same result whether it is the first or subsequent times
	running the function. Maturing."""

	cran = "Require"

	maintainers("dorton21")

	version("0.3.1", md5="4c64508fb4a65aacbc530286fc5ed434")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-data-table@1.10.4:", type=("build", "run"))
