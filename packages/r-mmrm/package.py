# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmrm(RPackage):
	"""Mixed Models for Repeated Measures

	Mixed models for repeated measures (MMRM) are a popular
    choice for analyzing longitudinal continuous outcomes in randomized
    clinical trials and beyond; see Cnaan, Laird and Slasor (1997)
    <doi:10.1002/(SICI)1097-0258(19971030)16:20%3C2349::AID-SIM667%3E3.0.CO;2-E>
    for a tutorial and Mallinckrodt, Lane, Schnell, Peng and Mancuso
    (2008) <doi:10.1177/009286150804200402> for a review. This package
    implements MMRM based on the marginal linear model without random
    effects using Template Model Builder ('TMB') which enables fast and
    robust model fitting. Users can specify a variety of covariance
    matrices, weight observations, fit models with restricted or standard
    maximum likelihood inference, perform hypothesis testing with
    Satterthwaite or Kenward-Roger adjustment, and extract least square
    means estimates by using 'emmeans'.
	"""
	
	homepage = "https://openpharma.github.io/mmrm/"
	cran = "mmrm" 

	version("0.3.10", md5="2de54950b4f18ead8802f637b819ba06")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-checkmate@2:", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tmb@1.9.1:", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
