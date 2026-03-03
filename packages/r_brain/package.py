# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrain(RPackage):
	"""Baffling Recursive Algorithm for Isotope distributioN calculations

	Package for calculating aggregated isotopic distribution and exact center-masses for chemical substances (in this version composed of C, H, N, O and S). This is an implementation of the BRAIN algorithm described in the paper by J. Claesen, P. Dittwald, T. Burzykowski and D. Valkenborg.
	"""
	
	bioc = "BRAIN" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BRAIN_1.48.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BRAIN/BRAIN_1.48.0.tar.gz"]

	version("1.48.0", md5="575b879f058d01202c3bc33b0ff8e3f1")

	depends_on("r@2.8.1:", type=("build", "run"))
	depends_on("r-polynomf", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
