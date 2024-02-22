# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcparalleldo(RPackage):
	"""A Simplified Interface for Running Commands on Parallel
Processes

	Provides a function that wraps 
    mcparallel() and mccollect() from 'parallel' with temporary variables and a 
    task handler.  Wrapped in this way the results of an mcparallel() call 
    can be returned to the R session when the fork is complete 
    without explicitly issuing a specific mccollect() to retrieve the value.
    Outside of top-level tasks, multiple mcparallel() jobs can be retrieved with 
    a single call to mcparallelDoCheck().
	"""
	
	homepage = "https://github.com/drknexus/mcparallelDo"
	cran = "mcparallelDo" 

	version("1.1.0", md5="df6ac81e08f34ff7c0c1091757169a52")

	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-checkmate@1.6.3:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
