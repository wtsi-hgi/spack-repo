# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidycmprsk(RPackage):
	"""Competing Risks Estimation

	Provides an intuitive interface for working with the
    competing risk endpoints. The package wraps the 'cmprsk' package, and
    exports functions for univariate cumulative incidence estimates and
    competing risk regression. Methods follow those introduced in Fine and
    Gray (1999) <doi:10.1002/sim.7501>.
	"""
	
	homepage = "https://mskcc-epi-bio.github.io/tidycmprsk/"
	cran = "tidycmprsk" 

	version("1.0.0", md5="07b08885cf0ecfdce85ae44f049d0c12")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-broom@1.0.1:", type=("build", "run"))
	depends_on("r-cli@3.1:", type=("build", "run"))
	depends_on("r-cmprsk@2.2.10:", type=("build", "run"))
	depends_on("r-dplyr@1.0.7:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-gtsummary@1.7.2:", type=("build", "run"))
	depends_on("r-hardhat@1.3:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-tibble@3.1.6:", type=("build", "run"))
	depends_on("r-tidyr@1.1.4:", type=("build", "run"))
