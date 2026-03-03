# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVoi(RPackage):
	"""Expected Value of Information

	Methods to calculate the expected value of information from a decision-analytic model.  This includes the expected value of perfect information (EVPI), partial perfect information (EVPPI) and sample information (EVSI), and the expected net benefit of sampling (ENBS).  A range of alternative computational methods are provided under the same user interface.  See Jackson et al. (2022) <doi:10.1146/annurev-statistics-040120-010730>.
	"""
	
	homepage = "https://chjackson.github.io/voi/"
	cran = "voi" 

	version("1.0.2", md5="17bc70da9584b0e61a0ff3d2bd6f8668")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-earth", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-dbarts", type=("build", "run"))
	depends_on("r-posterior", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
