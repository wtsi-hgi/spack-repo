# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDorothea(RPackage):
	"""Collection Of Human And Mouse TF Regulons

	DoRothEA is a gene regulatory network containing signed transcription factor (TF) - target gene interactions. DoRothEA regulons, the collection of a TF and its transcriptional targets, were curated and collected from different types of evidence for both human and mouse. A confidence level was assigned to each TF-target interaction based on the number of supporting evidence.
	"""
	
	homepage = "https://saezlab.github.io/dorothea/"
	bioc = "dorothea" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/dorothea_1.14.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/dorothea/dorothea_1.14.0.tar.gz"]

	version("1.14.0", md5="d1ad1213db5d54f1fc6ef8d195b9bbc0")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-bcellviper", type=("build", "run"))
	depends_on("r-decoupler", type=("build", "run"))

	# experiment