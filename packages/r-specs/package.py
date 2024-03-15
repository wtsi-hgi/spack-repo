# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpecs(RPackage):
	"""Single-Equation Penalized Error-Correction Selector (SPECS)

	Implementation of SPECS, your favourite Single-Equation Penalized Error-Correction Selector developed in
    Smeekes and Wijler (2021) <doi:10.1016/j.jeconom.2020.07.021>. SPECS provides a fully automated estimation procedure for large and potentially
    (co)integrated datasets. The dataset in levels is converted to a conditional error-correction model, either by the user or
    by means of the functions included in this package, and various specialised forms of penalized regression can be applied to
    the model. Automated options for initializing and selecting a sequence of penalties, as well as the construction of penalty
    weights via an initial estimator, are available. Moreover, the user may choose from a number of pre-specified deterministic
    configurations to further simplify the model building process.
	"""
	
	cran = "specs" 

	version("1.0.1", md5="0a3100177c3bc968ed9d0dc0015280ca")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
