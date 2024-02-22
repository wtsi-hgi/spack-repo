# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBprinstrattte(RPackage):
	"""Causal Effects in Principal Strata Defined by Antidrug
Antibodies

	Bayesian models to estimate causal effects of biological 
    treatments on time-to-event endpoints in clinical trials with principal
    strata defined by the occurrence of antidrug antibodies. 
    The methodology is based on Frangakis and Rubin (2002) 
    <doi:10.1111/j.0006-341x.2002.00021.x> and Imbens and Rubin (1997)
    <doi:10.1214/aos/1034276631>, and intended to be applied to a
    specific time-to-event setting.
	"""
	
	homepage = "https://github.com/Boehringer-Ingelheim/BPrinStratTTE"
	cran = "BPrinStratTTE" 

	version("0.0.2", md5="ae410aaa95bc69b64bf7b8f0b0738d8a")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
	depends_on("r-rstantools", type=("build", "link", "run"))
