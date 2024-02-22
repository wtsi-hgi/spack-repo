# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdmiral(RPackage):
	"""ADaM in R Asset Library

	A toolbox for programming Clinical Data Interchange Standards
    Consortium (CDISC) compliant Analysis Data Model (ADaM) datasets in R.
    ADaM datasets are a mandatory part of any New Drug or Biologics
    License Application submitted to the United States Food and Drug
    Administration (FDA). Analysis derivations are implemented in
    accordance with the "Analysis Data Model Implementation Guide" (CDISC
    Analysis Data Model Team, 2021,
    <https://www.cdisc.org/standards/foundational/adam>).
	"""
	
	homepage = "https://pharmaverse.github.io/admiral/"
	cran = "admiral" 

	version("1.0.1", md5="a0c89b5666983480dbfbcd05269ad90c")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-admiraldev@1:", type=("build", "run"))
	depends_on("r-dplyr@1.0.5:", type=("build", "run"))
	depends_on("r-hms@0.5.3:", type=("build", "run"))
	depends_on("r-lifecycle@0.1:", type=("build", "run"))
	depends_on("r-lubridate@1.7.4:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr@0.3.3:", type=("build", "run"))
	depends_on("r-rlang@0.4.4:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tidyr@1.0.2:", type=("build", "run"))
	depends_on("r-tidyselect@1.1:", type=("build", "run"))
