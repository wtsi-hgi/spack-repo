# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHealthfinance(RPackage):
	"""Financial Projections and Planning for Health Care Practices

	Provides a shiny interface for a free, open-source managerial
    accounting-like system for health care practices. This package allows
    health care administrators to project revenue with monthly adjustments
    and procedure-specific boosts up to a 3-year period. Granular data
    (patient-level) to aggregated data (department- or hospital-level) can
    all be used as valid inputs provided historical volume and revenue
    data is available. For more details on managerial accounting
    techniques, see Brewer et al. (2015, ISBN:9780078025792).
	"""
	
	homepage = "https://rrrlw.github.io/healthfinance/"
	cran = "healthfinance" 

	version("0.1.0", md5="b1b6d7154f88e1a4e7e2197163e00069")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-lubridate@1.7:", type=("build", "run"))
	depends_on("r-readr@1.3:", type=("build", "run"))
	depends_on("r-scales@1.1:", type=("build", "run"))
	depends_on("r-shiny@1.4:", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
