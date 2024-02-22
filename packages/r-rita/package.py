# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRita(RPackage):
	"""Automated Transformations, Normality Testing, and Reporting

	
    Automated performance of common transformations used to fulfill parametric
    assumptions of normality and identification of the best performing method 
    for the user. Output for various normality tests (Thode, 2002) corresponding 
    to the best performing method and a descriptive statistical report of the 
    input data in its original units (5-number summary and mathematical moments) 
    are also presented. Lastly, the Rankit, an empirical normal quantile transformation 
    (ENQT) (Soloman & Sawilowsky, 2009), is provided to accommodate non-standard 
    use cases and facilitate adoption.  
    <DOI: 10.1201/9780203910894>.
    <DOI: 10.22237/jmasm/1257034080>.
	"""
	
	cran = "Rita" 

	version("1.2.0", md5="d00f91ecf3c1588afb7115f6c10e4da5")

	depends_on("r-lattice", type=("build", "run"))
