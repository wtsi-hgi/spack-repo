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

	version("1.24.0", commit="a2e2c91dbbd40c8cf2224d6e070413aeb6bfb30d")
	version("1.18.0", commit="2b2f6344438667f408f70623aea68e541bc9d869")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcppalgos", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
