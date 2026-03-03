# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhyloseqgraphtest(RPackage):
	"""Graph-Based Permutation Tests for Microbiome Data

	Provides functions for graph-based multiple-sample
    testing and visualization of microbiome data, in particular data
    stored in 'phyloseq' objects. The tests are based on those
    described in Friedman and Rafsky (1979)
    <http://www.jstor.org/stable/2958919>, and the tests are described
    in more detail in Callahan et al. (2016)
    <doi:10.12688/f1000research.8986.1>.
	"""
	
	homepage = "https://github.com/jfukuyama/phyloseqGraphTest"
	cran = "phyloseqGraphTest" 

	version("0.1.1", md5="f3250337bc6d7a80bd842e9f382f4960")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-phyloseq@1.24:", type=("build", "run"))
	depends_on("r-ggnetwork@0.5.1:", type=("build", "run"))
	depends_on("r-igraph@1.1.2:", type=("build", "run"))
