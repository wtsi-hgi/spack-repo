# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTseind(RPackage):
	"""Total Survey Error (Independent Samples)

	Calculates total survey error (TSE) for one or more surveys, using both scale-dependent and scale-independent metrics.  Package works directly from the data set, with no hand calculations required: just upload a properly structured data set (see TESTIND and its documentation), properly input column names (see functions documentation), and run your functions.  For more on TSE, see: Weisberg, Herbert (2005, ISBN:0-226-89128-3); Biemer, Paul (2010) <doi:10.1093/poq/nfq058>; Biemer, Paul et.al. (2017, ISBN:9781119041672); etc.
	"""
	
	cran = "TSEind" 

	version("0.1.0", md5="1bfd441ff57ac4d8255fbf68e3394995")

	depends_on("r@3.5:", type=("build", "run"))
