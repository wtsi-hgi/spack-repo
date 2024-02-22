# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFuzzyPValue(RPackage):
	"""Computing Fuzzy p-Value

	The main goal of this package is drawing the membership function of the fuzzy p-value which is defined as a fuzzy set on the unit interval for three following problems: (1) testing crisp hypotheses based on fuzzy data, (2) testing fuzzy hypotheses based on crisp data, and (3) testing fuzzy hypotheses based on fuzzy data. In all cases, the fuzziness of data or/and the fuzziness of the boundary of null fuzzy hypothesis transported via the p-value function and causes to produce the fuzzy p-value. If the p-value is fuzzy, it is more appropriate to consider a fuzzy significance level for the problem. Therefore, the comparison of the fuzzy p-value and the fuzzy significance level is evaluated by a fuzzy ranking method in this package.
	"""
	
	cran = "Fuzzy.p.value" 

	version("1.1", md5="7c8596eb963d93c59d05ae3db61df5a8")

	depends_on("r-fuzzynumbers", type=("build", "run"))
