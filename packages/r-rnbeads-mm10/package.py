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

	version("2.16.0", tag="RELEASE_3_21")
	version("2.10.0", sha256="28b28ad3b3521da37bd630b3c540dd2ad539435c34ba5cd3988234c5dbeb3674", url="https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/RnBeads.mm10_2.10.0.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))

