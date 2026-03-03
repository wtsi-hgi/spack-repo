# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnbeadsMm10(RPackage):
	"""RnBeads.mm10

	Automatically generated RnBeads annotation package for the assembly mm10.
	"""
	
	bioc = "RnBeads.mm10" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/RnBeads.mm10_2.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/RnBeads.mm10/RnBeads.mm10_2.10.0.tar.gz"]

	version("2.10.0", md5="0c935572ce46183bc5a7aaea31ea2519", url="https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/RnBeads.mm10_2.10.0.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))

