# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImaginator(RPackage):
	"""Simulate General Insurance Policies and Losses

	Simulate general insurance policies, losses and loss emergence. The functions contemplate 
  deterministic and stochastic policy retention and growth scenarios. Retention and growth rates are percentages relative
  to the expiring portfolio. Claims are simulated for each policy. This is accomplished either be assuming a frequency
  distribution per development lag or by generating random wait times until claim emergence and settlement. Loss simulation 
  uses standard loss distributions for claim amounts.
	"""
	
	homepage = "https://github.com/casact/imaginator"
	cran = "imaginator" 

	version("1.0.0", md5="a409a216c15f5e99fe5b8cf84720a6c1")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-distributions3", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
