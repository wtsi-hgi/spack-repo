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
	version("0.3.0", sha256="de879999f71bd3009b58676673f26774119fa84d3d7fcc28d0b02f07d5c63968")
	version("0.1.4", sha256="1657dacff807ec8865892fce4d55cec9e31affafd90cb44ab59b704d29575a8c")
	version("0.1.2", sha256="c045c1cc69f6d6248306d88f6399699b9f86134a71b631e35b9101901593af1b")
	version("0.0.13", sha256="ad9cb167694abe70beadc972c2c25086f0ac8e7e5802bf9606c1868e01be2526")
	version("0.0.10", sha256="2087c3bb4d660d205962e241c1fc4a366dada5a1ed090d545c52188490567f8d")
	version("0.3.1", md5="4c64508fb4a65aacbc530286fc5ed434")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-data-table@1.10.4:", type=("build", "run"))
