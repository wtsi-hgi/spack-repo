# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHttr(RPackage):
	"""Tools for Working with URLs and HTTP.

	Useful tools for working with HTTP organised by HTTP verbs (GET(), POST(),
	etc). Configuration functions make it easy to control additional request
	components (authenticate(), add_headers() and so on)."""

	cran = "httr"

	version("1.4.7", md5="8965ffef86aea39922f435c019daf9fb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-curl@5.0.2:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-mime", type=("build", "run"))
	depends_on("r-openssl@0.8:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
