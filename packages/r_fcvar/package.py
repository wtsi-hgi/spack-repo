# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFcvar(RPackage):
	"""Estimation and Inference for the Fractionally Cointegrated VAR

	Estimation and inference using the Fractionally Cointegrated 
    Vector Autoregressive (VAR) model. It includes functions for model specification, 
    including lag selection and cointegration rank selection, as well as a comprehensive
    set of options for hypothesis testing, including tests of hypotheses on the 
    cointegrating relations, the adjustment coefficients and the fractional 
    differencing parameters. 
    An article describing the FCVAR model with examples is available on the Webpage 
    <https://sites.google.com/view/mortennielsen/software>.
	"""
	
	homepage = "https://github.com/LeeMorinUCF/FCVAR"
	cran = "FCVAR" 

	version("0.1.4", md5="449e94dc62505a104115f6ed878e8133")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-fracdist", type=("build", "run"))
