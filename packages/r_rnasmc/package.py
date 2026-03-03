# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnasmc(RPackage):
	"""RNA Secondary Structure Module Mining, Comparison and Plotting

	Provides function for RNA secondary structure plotting, comparison and module mining. Given a RNA secondary structure, you can obtain stem regions, hairpin loops, internal loops, bulge loops and multibranch loops of this RNA structure using this program. They are the basic modules of RNA secondary structure. For each module you get, you can use this program to label the RNA structure with a specific color. You can also use this program to compare two RNA secondary structures to get a score that represents similarity. Reference: Reuter JS, Mathews DH (2010) <doi:10.1186/1471-2105-11-129>.
	"""
	
	cran = "RNAsmc" 

	version("0.8.0", md5="a1c3276b1b9844d64079ee5ecd393030")

	depends_on("r-rrna", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
