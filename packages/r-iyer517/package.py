# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIyer517(RPackage):
	"""exprSets for Iyer, Eisen et all 1999 Science paper

	representation of public Iyer data from http://genome-www.stanford.edu/serum/clusters.html
	"""
	
	bioc = "Iyer517"

	version("1.50.0", commit="86347bbb14cbb868e54032bcccc82ad6d89675eb")
	version("1.44.0", commit="79647a5178a6bbabe06778f734989f4f5643906e")

	depends_on("r-biobase@2.5.5:", type=("build", "run"))

