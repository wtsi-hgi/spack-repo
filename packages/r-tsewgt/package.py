# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsewgt(RPackage):
	"""Total Survey Error Under Multiple, Different Weighting Schemes

	Calculates total survey error (TSE) for a survey under multiple, different weighting schemes, using both scale-dependent and scale-independent metrics.  Package works directly from the data set, with no hand calculations required: just upload a properly structured data set (see TESTWGT and its documentation), properly input column names (see functions documentation), and run your functions.  For more on TSE, see: Weisberg, Herbert (2005, ISBN:0-226-89128-3); Biemer, Paul (2010) <doi:10.1093/poq/nfq058>; Biemer, Paul et.al. (2017, ISBN:9781119041672); etc.
	"""
	
	cran = "TSEwgt" 

	version("0.1.0", md5="57064bc16326d7294ebd572c535ac6a9")

	depends_on("r@3.5:", type=("build", "run"))
