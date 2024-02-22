# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDabestr(RPackage):
	"""Data Analysis using Bootstrap-Coupled Estimation

	Data Analysis using Bootstrap-Coupled ESTimation.
  Estimation statistics is a simple framework that avoids the pitfalls of
  significance testing. It uses familiar statistical concepts: means,
  mean differences, and error bars. More importantly, it focuses on the
  effect size of one's experiment/intervention, as opposed to a false
  dichotomy engendered by P values.
  An estimation plot has two key features:
  1. It presents all datapoints as a swarmplot, which orders each point to
  display the underlying distribution.
  2. It presents the effect size as a bootstrap 95% confidence interval on a
  separate but aligned axes.
  Estimation plots are introduced in Ho et al., Nature Methods 2019, 1548-7105.
  <doi:10.1038/s41592-019-0470-3>.
  The free-to-view PDF is located at <https://www.nature.com/articles/s41592-019-0470-3.epdf?author_access_token=Euy6APITxsYA3huBKOFBvNRgN0jAjWel9jnR3ZoTv0Pr6zJiJ3AA5aH4989gOJS_dajtNr1Wt17D0fh-t4GFcvqwMYN03qb8C33na_UrCUcGrt-Z0J9aPL6TPSbOxIC-pbHWKUDo2XsUOr3hQmlRew%3D%3D>.
	"""
	
	homepage = "https://github.com/ACCLAB/dabestr"
	cran = "dabestr" 

	version("2023.9.12", md5="95dee9b5e437f9455c7bfb9151c051c9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggbeeswarm", type=("build", "run"))
	depends_on("r-effsize", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ggsci", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-brunnermunzel", type=("build", "run"))
