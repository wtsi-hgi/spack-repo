# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCcl4(RPackage):
	"""Carbon Tetrachloride (CCl4) treated hepatocytes

	NChannelSet for rat hepatocytes treated with Carbon Tetrachloride (CCl4) data from LGC company.
	"""
	
	bioc = "CCl4" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/CCl4_1.40.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/CCl4/CCl4_1.40.0.tar.gz"]

	version("1.40.0", md5="3247cf1db347f959d908e88b5e8febb5", url="https://www.bioconductor.org/packages/release/data/experiment/src/contrib/CCl4_1.40.0.tar.gz")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))

	# experiment