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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MotifDb_1.44.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MotifDb/MotifDb_1.44.0.tar.gz"]

	version("1.44.0", sha256="b90fed332c52bcceed296b824867ab944ebab291863926bf994a403d5c71e2fc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-splitstackshape", type=("build", "run"))
