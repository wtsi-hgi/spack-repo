# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDials(RPackage):
	"""Tools for Creating Tuning Parameter Values

	Many models contain tuning parameters (i.e. parameters that
    cannot be directly estimated from the data). These tools can be used
    to define objects for creating, simulating, or validating values for
    such parameters.
	"""
	
	homepage = "https://dials.tidymodels.org"
	cran = "dials" 

	version("1.2.1", md5="71af0aae8351ff80de1e3d8c55f5c135")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-scales@1.3:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dicedesign", type=("build", "run"))
	depends_on("r-dplyr@0.8.5:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-hardhat@1.1:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-vctrs@0.3.8:", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
