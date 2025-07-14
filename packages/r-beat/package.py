# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBeat(RPackage):
	"""BEAT - BS-Seq Epimutation Analysis Toolkit

	Model-based analysis of single-cell methylation data
	"""
	
	bioc = "BEAT" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BEAT_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BEAT/BEAT_1.40.0.tar.gz"]

	version("1.46.0", tag="RELEASE_3_21")
	version("1.40.0", sha256="ba27bdfeb7bab351b7590e1473a026bee73d93e4e6daf89aef6d5f91e8a5accf")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-shortread", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
