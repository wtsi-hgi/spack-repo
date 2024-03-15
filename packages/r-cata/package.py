# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCata(RPackage):
	"""Analysis of Check-All-that-Apply (CATA) Data

	Functions for analyzing check-all-that-apply (CATA) data from consumer and sensory tests. Cochran's Q test, McNemar's test, and Penalty-Lift analysis provided, as described in for CATA data analysis by Meyners, Castura & Carr (2013) <doi:10.1016/j.foodqual.2013.06.010>. Cluster analysis can be performed using b-cluster analysis. The quality of cluster analysis solutions can be evaluated using various measures. The methods related to b-cluster analysis are described in a manuscript by Castura, Meyners, Varela & Næs (2022) <doi:10.1016/j.foodqual.2022.104564>. Methods are adapted to product-related hedonic responses by Castura, Meyners, Pohjanheimo, Varela & Næs (2023) <doi:10.1111/joss.12860>. 
	"""
	
	cran = "cata" 

	version("0.1.0.5", md5="27d2849d9089c5e14d66d0b096f84e93")

	depends_on("r@4.2:", type=("build", "run"))
