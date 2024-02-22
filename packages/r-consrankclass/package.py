# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConsrankclass(RPackage):
	"""Classification and Clustering of Preference Rankings

	Tree-based classification and soft-clustering method for preference rankings, with tools for external validation of fuzzy clustering.
    It contains the recursive partitioning algorithm for preference rankings, non-parametric tree-based method for a matrix of preference rankings as a response variable. It contains also the distribution-free soft clustering method for preference rankings, namely the K-median cluster component analysis (CCA). 
    The package depends on the 'ConsRank' R package.
    Options for validate the tree-based method are both test-set procedure and V-fold cross validation.
    The package contains the routines to compute the adjusted concordance index (a fuzzy version of the adjusted rand index) and the normalized degree of concordance (the corresponding fuzzy version of the rand index).
    Essential references:
    D'Ambrosio, A., Amodio, S., Iorio, C., Pandolfo, G., and Siciliano, R. (2021) <doi:10.1007/s00357-020-09367-0>
    D'Ambrosio, A., and Heiser, W.J. (2019) <doi:10.1007/s41237-018-0069-5>;    
    D'Ambrosio, A., and Heiser W.J. (2016) <doi:10.1007/s11336-016-9505-1>;
    Hullermeier, E., Rifqi, M., Henzgen, S., and Senge, R. (2012) <doi:10.1109/TFUZZ.2011.2179303>.
	"""
	
	homepage = "https://www.r-project.org/"
	cran = "ConsRankClass" 

	version("1.0.1", md5="fd98864ce864baaaf5969ce2eb8ee03b")

	depends_on("r-consrank", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
