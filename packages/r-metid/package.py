# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetid(RPackage):
	"""Network-based prioritization of putative metabolite IDs

	This package uses an innovative network-based approach that will enhance our ability to determine the identities of significant ions detected by LC-MS.
	"""
	
	homepage = "https://github.com/ressomlab/MetID"
	bioc = "MetID" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MetID_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MetID/MetID_1.20.0.tar.gz"]

	version("1.20.0", sha256="141fea94d2b32369b8d1e60eaf809d3390c5a5f9bd92bac0d6d86aab9c69a58d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-devtools@1.13:", type=("build", "run"))
	depends_on("r-stringr@1.3:", type=("build", "run"))
	depends_on("r-matrix@1.2.12:", type=("build", "run"))
	depends_on("r-igraph@1.2.1:", type=("build", "run"))
	depends_on("r-chemminer@2.30.2:", type=("build", "run"))
