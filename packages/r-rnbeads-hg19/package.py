# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnbeadsHg19(RPackage):
	"""RnBeads.hg19

	Automatically generated RnBeads annotation package for the assembly hg19.
	"""
	
	bioc = "RnBeads.hg19" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/RnBeads.hg19_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/RnBeads.hg19/RnBeads.hg19_1.34.0.tar.gz"]

    version("1.40.0", tag="RELEASE_3_21")
	version("1.34.0", sha256="26b2c7cd893c78a9475aa812cf2dfa7b5e1b0f4ba702d8c4c18d470e27be6657", url="https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/RnBeads.hg19_1.34.0.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))

