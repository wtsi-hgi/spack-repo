# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRagtop(RPackage):
	"""Pricing Equity Derivatives with Extensions of Black-Scholes

	Algorithms to price American and European
    equity options, convertible bonds and a
    variety of other financial derivatives. It uses an
    extension of the usual Black-Scholes model in which
    jump to default may occur at a probability specified
    by a power-law link between stock price and hazard
    rate as found in the paper by Takahashi, Kobayashi,
    and Nakagawa (2001) <doi:10.3905/jfi.2001.319302>.  We
    use ideas and techniques from Andersen and
    Buffum (2002) <doi:10.2139/ssrn.355308> and
    Linetsky (2006) <doi:10.1111/j.1467-9965.2006.00271.x>.
	"""
	
	cran = "ragtop" 

	version("1.1.1", md5="dcb7e216eb8662759a2fa49056dde2b2")

	depends_on("r-limsolve@1.5.5.1:", type=("build", "run"))
	depends_on("r-futile-logger@1.4.1:", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
