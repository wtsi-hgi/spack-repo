# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsmstests(RPackage):
	"""LC-MS/MS Differential Expression Tests

	Statistical tests for label-free LC-MS/MS data by spectral counts, to discover differentially expressed proteins between two biological conditions. Three tests are available: Poisson GLM regression, quasi-likelihood GLM regression, and the negative binomial of the edgeR package.The three models admit blocking factors to control for nuissance variables.To assure a good level of reproducibility a post-test filter is available, where we may set the minimum effect size considered biologicaly relevant, and the minimum expression of the most abundant condition.
	"""
	
	bioc = "msmsTests" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/msmsTests_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/msmsTests/msmsTests_1.40.0.tar.gz"]

	version("1.40.0", md5="90c08df612ce3e4608ab3b9fa048764a")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-msnbase", type=("build", "run"))
	depends_on("r-msmseda", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
