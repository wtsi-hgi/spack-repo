# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVtpnet(RPackage):
	"""variant-transcription factor-phenotype networks

	variant-transcription factor-phenotype networks, inspired by Maurano et al., Science (2012), PMID 22955828
	"""
	
	bioc = "vtpnet"

	version("0.48.0", commit="2c9d36f770981e3f86218f91b3a1bc57a3fef81f")
	version("0.42.0", commit="6460d61018317841870d6acbfec5320263d5a12b")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-gwascat", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
