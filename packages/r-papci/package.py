# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPapci(RPackage):
	"""Prevalence Adjusted PPV Confidence Interval

	Positive predictive value (PPV) defined as the conditional probability of clinical trial assay (CTA) being positive given Companion diagnostic device (CDx) being positive is a key performance parameter for evaluating the clinical validity utility of a companion diagnostic test in clinical bridging studies. When bridging study patients are enrolled based on CTA assay results, Binomial-based confidence intervals (CI) may are not appropriate for PPV CI estimation. Bootstrap CIs which are not restricted by the Binomial assumption may be used for PPV CI estimation only when PPV is not 100%. Bootstrap CI is not valid when PPV is 100% and becomes a single value of [1, 1]. We proposed a risk ratio-based method for constructing CI for PPV. By simulation we illustrated that the coverage probability of the proposed CI is close to the nominal value even when PPV is high and negative percent agreement (NPA) is close to 100%. There is a lack of R package for PPV CI calculation. we developed a publicly available R package along with this shiny app to implement the proposed approach and some other existing methods.
	"""
	
	cran = "papci" 

	version("0.1.0", md5="2c1dc9635e054c43d4bcfa78d981362a")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-binom", type=("build", "run"))
	depends_on("r-propcis", type=("build", "run"))
	depends_on("r-ratesci", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
