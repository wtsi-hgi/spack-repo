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

	version("1.60.0", md5="b30abc9c50034b41daf1399031d657e3")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
