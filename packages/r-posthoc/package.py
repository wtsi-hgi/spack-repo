# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPosthoc(RPackage):
	"""Tools for Post-Hoc Analysis

	Implements a range of facilities for post-hoc analysis and
             summarizing linear models, generalized linear models and 
             generalized linear mixed models, including grouping and clustering 
             via pairwise comparisons using graph representations and efficient
             algorithms for finding maximal cliques of a graph. 
             Includes also non-parametric toos for post-hoc analysis.
             It has S3 methods for printing summarizing, and producing plots, 
             line and barplots suitable for post-hoc analyses. 
	"""
	
	homepage = "https://tildeweb.au.dk/au33031/astatlab/software/posthoc"
	cran = "postHoc" 

	version("0.1.3", md5="ce179231c2977fdfce881dcc0888b44f")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
