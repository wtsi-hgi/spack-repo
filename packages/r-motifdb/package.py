# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMotifdb(RPackage):
	"""An Annotated Collection of Protein-DNA Binding Sequence Motifs

	More than 9900 annotated position frequency matrices from 14 public sources, for multiple organisms.
	"""
	
	bioc = "MotifDb"

	version("1.50.0", commit="9b7c5d1b558f4b834b9ec99c88e9a6d4d58c91e1")
	version("1.44.0", commit="12d072e99ac0642cd334b3512abca7f2578ff553")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-splitstackshape", type=("build", "run"))
