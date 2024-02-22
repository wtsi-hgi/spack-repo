# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFishalyser(RPackage):
	"""FISHalyseR a package for automated FISH quantification

	FISHalyseR provides functionality to process and analyse digital cell culture images, in particular to quantify FISH probes within nuclei. Furthermore, it extract the spatial location of each nucleus as well as each probe enabling spatial co-localisation analysis.
	"""
	
	bioc = "FISHalyseR" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/FISHalyseR_1.36.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/FISHalyseR/FISHalyseR_1.36.0.tar.gz"]

	version("1.36.0", md5="fea17ba4629a7d53c62eef47a3cdfab2")

	depends_on("r-ebimage", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
