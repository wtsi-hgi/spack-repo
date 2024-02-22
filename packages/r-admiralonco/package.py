# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdmiralonco(RPackage):
	"""Oncology Extension Package for ADaM in 'R' Asset Library

	Programming oncology specific Clinical Data Interchange Standards Consortium
    (CDISC) compliant Analysis Data Model (ADaM) datasets in 'R'. ADaM datasets are a
    mandatory part of any New Drug or Biologics License Application submitted to the
    United States Food and Drug Administration (FDA). Analysis derivations are
    implemented in accordance with the "Analysis Data Model Implementation Guide"
    (CDISC Analysis Data Model Team (2021), <https://www.cdisc.org/standards/foundational/adam>).
    The package is an extension package of the 'admiral' package.
	"""
	
	homepage = "https://pharmaverse.github.io/admiralonco/"
	cran = "admiralonco" 

	version("1.0.0", md5="446b266e9e6f0fea10ca12e2c77dab47")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-admiral@1:", type=("build", "run"))
	depends_on("r-admiraldev@1:", type=("build", "run"))
	depends_on("r-dplyr@0.8.4:", type=("build", "run"))
	depends_on("r-lifecycle@0.1:", type=("build", "run"))
	depends_on("r-lubridate@1.7.4:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-rlang@0.4.4:", type=("build", "run"))
	depends_on("r-tidyselect@1:", type=("build", "run"))
