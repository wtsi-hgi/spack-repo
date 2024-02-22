# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClinicalsignificance(RPackage):
	"""A Toolbox for Clinical Significance Analyses in Intervention
Studies

	A clinical significance analysis can be used to determine if an 
    intervention has a meaningful or practical effect for patients. You provide 
    a tidy data set plus a few more metrics and this package will take care of 
    it to make your results publication ready.
	"""
	
	homepage = "https://pedscience.github.io/clinicalsignificance/"
	cran = "clinicalsignificance" 

	version("2.0.0", md5="2695ccfa96556eea0bbd84ed9f4374f8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-bayesfactor", type=("build", "run"))
	depends_on("r-bayestestr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-insight", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
