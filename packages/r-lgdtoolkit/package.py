# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLgdtoolkit(RPackage):
	"""Collection of Tools for LGD Rating Model Development

	The goal of this package is to cover the most common steps in Loss Given Default (LGD) rating model development.
             The main procedures available are those that refer to bivariate and multivariate analysis. In particular two statistical methods for 
             multivariate analysis are currently implemented – OLS regression and fractional logistic regression.
             Both methods are also available within different blockwise model designs and both have customized stepwise algorithms. 
             Descriptions of these customized designs are available in Siddiqi (2016) <doi:10.1002/9781119282396.ch10> and 
             Anderson, R.A. (2021) <doi:10.1093/oso/9780192844194.001.0001>. 
             Although they are explained for PD model, the same designs are applicable for LGD model with different underlying regression methods 
             (OLS and fractional logistic regression). To cover other important steps for LGD model development, it is recommended to use 
             'LGDtoolkit' package along with 'PDtoolkit', and 'monobin' (or 'monobinShiny') packages.
             Additionally, 'LGDtoolkit' provides set of procedures handy for initial and periodical model validation. 
	"""
	
	homepage = "https://github.com/andrija-djurovic/LGDtoolkit"
	cran = "LGDtoolkit" 

	version("0.2.0", md5="65d5bf70fe0ecaf808373cd36efe4190")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-monobin", type=("build", "run"))
