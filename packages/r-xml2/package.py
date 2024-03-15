# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXml2(RPackage):
	"""Package required POI jars for the xlsx package.

	Work with XML files using a simple, consistent interface. Built on top of
	the 'libxml2' C library."""

	cran = "xml2"

	license("MIT")

	version("1.3.6", md5="fc6679028dca1f3047c8c745fb724524", url="https://cran.r-project.org/src/contrib/xml2_1.3.6.tar.gz")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("libxml2", type=("build", "link", "run"))
