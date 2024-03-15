# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXmapbridge(RPackage):
	"""Export plotting files to the xmapBridge for visualisation in X:Map.

	xmapBridge can plot graphs in the X:Map genome browser. This package
	exports plotting files in a suitable format."""

	bioc = "xmapbridge"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/xmapbridge_1.60.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/xmapbridge/xmapbridge_1.60.0.tar.gz"]

	version("1.60.0", md5="8b07bc6daa0d9dad8943ef442076eb5e")

	depends_on("r@2:", type=("build", "run"))
