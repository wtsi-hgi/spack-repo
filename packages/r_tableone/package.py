# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTableone(RPackage):
	"""Create 'Table 1' to Describe Baseline Characteristics with or
without Propensity Score Weights

	Creates 'Table 1', i.e., description of baseline patient
    characteristics, which is essential in every medical research.
    Supports both continuous and categorical variables, as well as
    p-values and standardized mean differences. Weighted data are
    supported via the 'survey' package.
	"""
	
	homepage = "https://github.com/kaz-yos/tableone"
	cran = "tableone" 

	version("0.13.2", md5="b46b9943bedcf516d8742ba3bd0d1743")

	depends_on("r-survey", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-gmodels", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-labelled", type=("build", "run"))
