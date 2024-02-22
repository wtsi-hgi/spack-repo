# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbgl(RPackage):
	"""An interface to the BOOST graph library.

	A fairly extensive and comprehensive interface to the graph algorithms
	contained in the BOOST library."""

	bioc = "RBGL"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/RBGL_1.78.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/RBGL/RBGL_1.78.0.tar.gz"]

	version("1.78.0", md5="a18b5ad5c49f058b6f65a2bd0a4274d1")

	depends_on("r-graph", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
