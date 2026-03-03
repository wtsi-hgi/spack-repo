# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimengine(RPackage):
	"""A Modular Framework for Statistical Simulations in R

	An open-source R package for structuring, maintaining, running, and debugging statistical simulations on both local and cluster-based computing environments.See full documentation at <https://avi-kenny.github.io/SimEngine/>.
	"""
	
	cran = "SimEngine" 

	version("1.3.0", md5="18b7b42c3b9b8d46a47639644a0be6c0")

	depends_on("r-magrittr@2.0.3:", type=("build", "run"))
	depends_on("r-dplyr@1.0.10:", type=("build", "run"))
	depends_on("r-pbapply@1.6:", type=("build", "run"))
	depends_on("r-data-table@1.14.6:", type=("build", "run"))
	depends_on("r-rlang@1.0.6:", type=("build", "run"))
