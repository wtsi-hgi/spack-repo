# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLongitudinalcascade(RPackage):
	"""Longitudinal Cascade

	Creates a series of sets of graphics and statistics related to the longitudinal cascade, all included in a single object. The longitudinal cascade inputs longitudinal data to identify gaps in the HIV and related cascades by observing differences using time to event and survival methods. The stage definitions are set by the user, with default standard options. Outputs include graphics, datasets, and formal statistical tests.
	"""
	
	cran = "longitudinalcascade" 

	version("0.3.2.6", md5="0faa951d103e205288c1fc296ec3cf59")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
