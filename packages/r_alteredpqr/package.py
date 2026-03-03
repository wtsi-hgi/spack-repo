# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlteredpqr(RPackage):
	"""Detection of Altered Protein Quantitative Relationships

	Inference of protein complex states from quantitative proteomics data. The package takes information on known stable protein interactions (i.e. protein components of the same complex) and assesses how protein quantitative ratios change between different conditions. It reports protein pairs for which relative protein quantities to each other have been significantly altered in the tested condition.
	"""
	
	cran = "AlteredPQR" 

	version("0.1.0", md5="ce3874311f39b8f4bf066114ccacc732")

	depends_on("r@3.5:", type=("build", "run"))
