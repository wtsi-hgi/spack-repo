# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPool(RPackage):
	"""Object Pooling.

	Enables the creation of object pools, which make it less computationally
	expensive to fetch a new object. Currently the only supported pooled
	objects are 'DBI' connections."""

	cran = "pool"

	license("MIT")

	version("1.0.3", md5="c9eb2149ca6294d2c120dddd77f1b6cc")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dbi@1.2.1:", type=("build", "run"))
	depends_on("r-later@1:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
