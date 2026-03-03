# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistatisr(RPackage):
	"""DiSTATIS Three Way Metric Multidimensional Scaling

	Implement DiSTATIS and CovSTATIS  (three-way multidimensional scaling).  DiSTATIS and CovSTATIS are used to analyze multiple distance/covariance matrices collected on the same set of observations. These methods are based on Abdi, H., Williams, L.J., Valentin, D., & Bennani-Dosse, M. (2012) <doi:10.1002/wics.198>.
	"""
	
	cran = "DistatisR" 

	version("1.1.1", md5="44afe9ae134a826a150f1a4bcb8d184d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-prettygraphs", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidytext", type=("build", "run"))
