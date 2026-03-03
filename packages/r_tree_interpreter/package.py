# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreeInterpreter(RPackage):
	"""Random Forest Prediction Decomposition and Feature Importance
Measure

	An R re-implementation of the 'treeinterpreter' package on PyPI
        <https://pypi.org/project/treeinterpreter/>. Each prediction can be
        decomposed as 'prediction = bias + feature_1_contribution + ... +
        feature_n_contribution'. This decomposition is then used to calculate
        the Mean Decrease Impurity (MDI) and Mean Decrease Impurity using
        out-of-bag samples (MDI-oob) feature importance measures based on the
        work of Li et al. (2019) <arXiv:1906.10845>.
	"""
	
	homepage = "https://github.com/nalzok/tree.interpreter"
	cran = "tree.interpreter" 

	version("0.1.1", md5="2d10a7d6ed383bef5d1169af005f4e09")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
