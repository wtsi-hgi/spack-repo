# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmericancallopt(RPackage):
	"""This package includes pricing function for selected American
call options with underlying assets that generate payouts

	This package includes a set of pricing functions for
        American call options. The following cases are covered: Pricing
        of an American call using the standard binomial approximation;
        Hedge parameters for an American call with a standard binomial
        tree; Binomial pricing of an American call with continuous
        payout from the underlying asset; Binomial pricing of an
        American call with an underlying stock that pays proportional
        dividends in discrete time; Pricing of an American call on
        futures using a binomial approximation; Pricing of a currency
        futures American call using a binomial approximation; Pricing
        of a perpetual American call. The user should kindly notice
        that this material is for educational purposes only. The codes
        are not optimized for computational efficiency as they are
        meant to represent standard cases of analytical and numerical
        solution.
	"""
	
	cran = "AmericanCallOpt" 

	version("0.95", md5="cd38a46a70ae1af7d26b22015258ccbc")

	depends_on("r@2:", type=("build", "run"))
