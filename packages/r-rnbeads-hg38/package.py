# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnbeadsHg38(RPackage):
	"""RnBeads.hg38

	Automatically generated RnBeads annotation package for the assembly hg38.
	"""
	
	bioc = "RnBeads.hg38" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/RnBeads.hg38_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/RnBeads.hg38/RnBeads.hg38_1.34.0.tar.gz"]

    version("1.40.0", tag="RELEASE_3_21")
	version("1.34.0", sha256="454c1a34cb3c9c1ebc66f792626b6aaf19258ca35506e054b056da386c3988a6", url="https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/RnBeads.hg38_1.34.0.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))

