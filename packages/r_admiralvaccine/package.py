# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdmiralvaccine(RPackage):
	"""Vaccine Extension Package for ADaM in 'R' Asset Library

	Programming vaccine specific Clinical Data Interchange
    Standards Consortium (CDISC) compliant Analysis Data Model (ADaM)
    datasets in 'R'. Flat model is followed as per 
    Center for Biologics Evaluation and Research (CBER) guidelines for
    creating vaccine specific domains. ADaM datasets are a mandatory part
    of any New Drug or Biologics License Application submitted to the
    United States Food and Drug Administration (FDA). Analysis derivations
    are implemented in accordance with the "Analysis Data Model
    Implementation Guide" (CDISC Analysis Data Model Team (2021),
    <https://www.cdisc.org/standards/foundational/adam/adamig-v1-3-release-package>).
    The package is an extension package of the 'admiral' package.
	"""
	
	homepage = "https://pharmaverse.github.io/admiralvaccine/"
	cran = "admiralvaccine" 

	version("0.2.0", md5="d21ca9f6fe5e17b095be5836a9ec6556")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-admiral@1:", type=("build", "run"))
	depends_on("r-admiraldev@1:", type=("build", "run"))
	depends_on("r-assertthat@0.2.1:", type=("build", "run"))
	depends_on("r-dplyr@0.8.4:", type=("build", "run"))
	depends_on("r-hms@0.5.3:", type=("build", "run"))
	depends_on("r-lifecycle@0.1:", type=("build", "run"))
	depends_on("r-lubridate@1.7.4:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-metatools", type=("build", "run"))
	depends_on("r-purrr@0.3.3:", type=("build", "run"))
	depends_on("r-rlang@0.4.4:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tidyr@1.0.2:", type=("build", "run"))
	depends_on("r-tidyselect@1:", type=("build", "run"))
