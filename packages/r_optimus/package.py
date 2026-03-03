# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptimus(RPackage):
	"""Model Based Diagnostics for Multivariate Cluster Analysis

	Assessment and diagnostics for comparing competing
    clustering solutions, using predictive models. The main intended
    use is for comparing clustering/classification solutions of
    ecological data (e.g. presence/absence, counts, ordinal scores) to
    1) find an optimal partitioning solution, 2) identify
    characteristic species and 3) refine a classification by merging
    clusters that increase predictive performance. However, in a more
    general sense, this package can do the above for any set of
    clustering solutions for i observations of j variables.
	"""
	
	homepage = "https://github.com/mitchest/optimus/"
	cran = "optimus" 

	version("0.2.0", md5="18a8453730ed6016a332776cf599378d")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mvabund@3.1:", type=("build", "run"))
	depends_on("r-ordinal@2015.1.21:", type=("build", "run"))
