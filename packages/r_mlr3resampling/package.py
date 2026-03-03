# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlr3resampling(RPackage):
	"""Resampling Algorithms for 'mlr3' Framework

	A supervised learning algorithm inputs a train set,
 and outputs a prediction function, which can be used on a test set.
 If each data point belongs to a group
 (such as geographic region, year, etc), then
 how do we know if it is possible to train on one group, and predict
 accurately on another group? Cross-validation can be used to determine
 the extent to which this is possible, by first assigning fold IDs from
 1 to K to all data (possibly using stratification, usually by group
 and label). Then we loop over test sets (group/fold combinations),
 train sets (same group, other groups, all groups), and compute
 test/prediction accuracy for each combination.  Comparing
 test/prediction accuracy between same and other, we can determine the
 extent to which it is possible (perfect if same/other have similar
 test accuracy for each group; other is usually somewhat less accurate
 than same; other can be just as bad as featureless baseline when the
 groups have different patterns).
 For more information, 
 <https://tdhock.github.io/blog/2023/R-gen-new-subsets/>
 describes the method in depth.
 How many train samples are required to get accurate predictions on a
 test set? Cross-validation can be used to answer this question, with
 variable size train sets.
	"""
	
	homepage = "https://github.com/tdhock/mlr3resampling"
	cran = "mlr3resampling" 

	version("2024.1.23", md5="db1d822abcc74d51662bb2cd39697972")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-paradox", type=("build", "run"))
	depends_on("r-mlr3", type=("build", "run"))
	depends_on("r-mlr3misc", type=("build", "run"))
