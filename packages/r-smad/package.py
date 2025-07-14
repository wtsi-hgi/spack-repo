# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmad(RPackage):
	"""Statistical Modelling of AP-MS Data (SMAD)

	Assigning probability scores to protein interactions captured in affinity purification mass spectrometry (AP-MS) expriments to infer protein-protein interactions. The output would facilitate non-specific background removal as contaminants are commonly found in AP-MS data.
	"""
	
	bioc = "SMAD" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SMAD_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SMAD/SMAD_1.18.0.tar.gz"]

    version("1.24.0", tag="RELEASE_3_21")
	version("1.18.0", sha256="877957cd9b9a582e60dfab8cad3814d034aff16f6f16bfe8cf2c610136e6f098")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcppalgos", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
