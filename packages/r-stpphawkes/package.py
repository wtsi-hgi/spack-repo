# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStpphawkes(RPackage):
	"""Missing Data for Marked Hawkes Process

	Estimation of model parameters for marked Hawkes process.
    Accounts for missing data in the estimation of the parameters.
    Technical details found in (Tucker et al., 2019 <DOI:10.1016/j.spasta.2018.12.004>).
	"""
	
	cran = "stpphawkes" 

	version("0.2.1", md5="bdfbd80f45ce6ad92b81328a609bbeb8")

	depends_on("r-interp", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-rcppgsl", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
