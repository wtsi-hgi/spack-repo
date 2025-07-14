# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCopyneutralima(RPackage):
	"""Copy Neutral Illumina Methylation Arrays

	Provides a set of genomic copy neutral samples hybridized using Illumina Methylation arrays (450k and EPIC).
	"""
	
	bioc = "CopyNeutralIMA" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/CopyNeutralIMA_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/CopyNeutralIMA/CopyNeutralIMA_1.20.0.tar.gz"]

    version("1.26.0", tag="RELEASE_3_21")
	version("1.20.0", sha256="5eb7c0a5b41557cc4b2f92665675866586c0297b12e7ba83c623a0082d498986")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-rdpack@0.8:", type=("build", "run"))

