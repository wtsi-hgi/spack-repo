# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdmiralophtha(RPackage):
	"""ADaM in R Asset Library - Ophthalmology

	Aids the programming of Clinical Data Standards Interchange Consortium
    (CDISC) compliant Ophthalmology Analysis Data Model (ADaM) datasets in R. ADaM datasets are a
    mandatory part of any New Drug or Biologics License Application submitted to the
    United States Food and Drug Administration (FDA). Analysis derivations are
    implemented in accordance with the "Analysis Data Model Implementation Guide"
    (CDISC Analysis Data Model Team, 2021, <https://www.cdisc.org/standards/foundational/adam/adamig-v1-3-release-package>).
	"""
	
	homepage = "https://pharmaverse.github.io/admiralophtha/"
	cran = "admiralophtha" 

	version("1.0.0", md5="f458fa43357a99265e42b07d6d735398")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-admiral", type=("build", "run"))
	depends_on("r-admiraldev", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-hms", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
