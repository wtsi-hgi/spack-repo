# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXml(RPackage):
	"""Tools for Parsing and Generating XML Within R and S-Plus.

	Many approaches for both reading and creating XML (and HTML) documents
	(including DTDs), both local and accessible via HTTP or FTP. Also offers
	access to an 'XPath' "interpreter"."""

	cran = "XML"

	version("3.99-0.16.1", md5="82344cf1059c2fd4f766ede4021836b2")

	depends_on("r@4:", type=("build", "run"))
	depends_on("libxml2@2.6.3:", type=("build", "link", "run"))
