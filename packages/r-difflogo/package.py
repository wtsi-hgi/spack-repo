# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDifflogo(RPackage):
	"""DiffLogo: A comparative visualisation of biooligomer motifs

	DiffLogo is an easy-to-use tool to visualize motif differences.
	"""
	
	homepage = "https://github.com/mgledi/DiffLogo/"
	bioc = "DiffLogo" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/DiffLogo_2.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/DiffLogo/DiffLogo_2.26.0.tar.gz"]

	version("2.32.0", tag="RELEASE_3_21")
	version("2.26.0", sha256="33da8346c4c056021a42eb5b1d22f7bf2752ff375ee54f2c5066a5e9ec3486c6")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-cba", type=("build", "run"))
