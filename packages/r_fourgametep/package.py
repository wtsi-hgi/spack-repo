# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFourgametep(RPackage):
	"""FourGamete Test

	The four-gamete test is based on the infinite-sites model which assumes that the probability of the same mutation occurring twice (recurrent or parallel mutations) and the probability of a mutation back to the original state (reverse mutations) are close to zero. Without these types of mutations, the only explanation for observing the four dilocus genotypes (example below) is recombination (Hudson and Kaplan 1985, Genetics 111:147-164). Thus, the presence of all four gametes is also called phylogenetic incompatibility.
	"""
	
	cran = "FourgameteP" 

	version("0.1.0", md5="90808278514c7a5d0e0b0564f270bdb1")

