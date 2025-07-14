# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHilbertvis(RPackage):
	"""Hilbert curve visualization

	Functions to visualize long vectors of integer data by means of Hilbert curves
	"""
	
	homepage = "http://www.ebi.ac.uk/~anders/hilbert"
	bioc = "HilbertVis" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/HilbertVis_1.60.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/HilbertVis/HilbertVis_1.60.0.tar.gz"]

    version("1.66.1", tag="RELEASE_3_21")
	version("1.60.0", sha256="96c7a4dfe42158e45bfb7a1e1a33e2577b23409249402cfa5ae742f2420060d5")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
