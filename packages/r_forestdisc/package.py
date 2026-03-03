# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForestdisc(RPackage):
	"""Forest Discretization

	Supervised, multivariate, and non-parametric discretization algorithm based on tree ensembles learning and moment matching optimization. This version of the algorithm relies on random forest algorithm to learn a large set of split points that conserves the relationship between attributes and the target class, and on moment matching optimization to transform this set into a reduced number of cut points matching as well as possible statistical properties of the initial set of split points. For each attribute to be discretized, the set S of its related split points extracted through random forest is mapped to a reduced set C of cut points of size k. This mapping relies on minimizing, for each continuous attribute to be discretized, the distance between the four first moments of S and the four first moments of C subject to some constraints. This non-linear optimization problem is performed using k values ranging from 2 to 'max_splits', and the best solution returned correspond to the value k which optimum solution is the lowest one over the different realizations. ForestDisc is a generalization of RFDisc discretization method initially proposed by Berrado and Runger (2009) <doi:10.1109/AICCSA.2009.5069327>, and improved by Berrado et al. in 2012 by adopting the idea of moment matching optimization related by Hoyland and Wallace (2001) <doi: 10.1287/mnsc.47.2.295.9834>.
	"""
	
	cran = "ForestDisc" 

	version("0.1.0", md5="08d497bf072128e80a0b82116fcb1d39")

	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
