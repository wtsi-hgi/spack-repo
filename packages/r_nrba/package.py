# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNrba(RPackage):
	"""Methods for Conducting Nonresponse Bias Analysis (NRBA)

	Facilitates nonresponse bias analysis (NRBA) 
    for survey data.  Such data may arise from a complex
    sampling design with features such as stratification, clustering, or
    unequal probabilities of selection. Multiple types of analyses may be
    conducted: comparisons of response rates across subgroups; comparisons
    of estimates before and after weighting adjustments; comparisons of
    sample-based estimates to external population totals; tests of
    systematic differences in covariate means between respondents
    and full samples; tests of independence between response status
    and covariates; and modeling of outcomes and response status as a 
    function of covariates. Extensive documentation and references are
    provided for each type of analysis. Krenzke, Van de Kerckhove,
    and Mohadjer (2005) <http://www.asasrms.org/Proceedings/y2005/files/JSM2005-000572.pdf>
    and Lohr and Riddles (2016) <https://www150.statcan.gc.ca/n1/en/pub/12-001-x/2016002/article/14677-eng.pdf?st=q7PyNsGR>
    provide an overview of the methods implemented in this package.
	"""
	
	cran = "nrba" 

	version("0.3.1", md5="4e50f6a239f00d042673fdce04669c4b")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-srvyr", type=("build", "run"))
	depends_on("r-survey@4.1.1:", type=("build", "run"))
	depends_on("r-svrep", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
