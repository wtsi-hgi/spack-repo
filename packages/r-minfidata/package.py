# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMinfidata(RPackage):
	"""Example data for the Illumina Methylation 450k array

	Data from 6 samples across 2 groups from 450k methylation arrays.
	"""
	
	bioc = "minfiData" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/minfiData_0.48.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/minfiData/minfiData_0.48.0.tar.gz"]

	version("0.48.0", md5="1ca7578aeab1a54db146c443870be6e7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-minfi@1.21.2:", type=("build", "run"))
	depends_on("r-illuminahumanmethylation450kmanifest", type=("build", "run"))
	depends_on("r-illuminahumanmethylation450kanno-ilmn12-hg19", type=("build", "run"))

	# experiment