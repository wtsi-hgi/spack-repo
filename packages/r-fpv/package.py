# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFpv(RPackage):
	"""Testing Hypotheses via Fuzzy P-Value in Fuzzy Environment

	The main goal of this package is drawing the membership function of the fuzzy p-value which is defined as a fuzzy set on the unit interval for three following problems: (1) testing crisp hypotheses based on fuzzy data, see Filzmoser and Viertl (2004) <doi:10.1007/s001840300269>, (2) testing fuzzy hypotheses based on crisp data, see Parchami et al. (2010) <doi:10.1007/s00362-008-0133-4>, and (3) testing fuzzy hypotheses based on fuzzy data, see Parchami et al. (2012) <doi:10.1007/s00362-010-0353-2>. In all cases, the fuzziness of data or / and the fuzziness of the boundary of null fuzzy hypothesis transported via the p-value function and causes to produce the fuzzy p-value. If the p-value is fuzzy, it is more appropriate to consider a fuzzy significance level for the problem. Therefore, the comparison of the fuzzy p-value and the fuzzy significance level is evaluated by a fuzzy ranking method in this package.
	"""
	
	cran = "FPV" 

	version("0.5", md5="2500989386995f6330beef6528c8dff3")

	depends_on("r-fuzzynumbers", type=("build", "run"))
	depends_on("r-fuzzynumbers-ext-2", type=("build", "run"))
