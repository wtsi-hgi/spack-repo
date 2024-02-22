# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRBlip(RPackage):
	"""Bayesian Network Learning Improved Project

	Allows the user to learn Bayesian networks from datasets containing thousands of variables. It focuses on score-based learning, mainly the 'BIC' and the 'BDeu' score functions. It provides state-of-the-art algorithms for the following tasks: (1) parent set identification - Mauro Scanagatta (2015) <http://papers.nips.cc/paper/5803-learning-bayesian-networks-with-thousands-of-variables>; (2) general structure optimization - Mauro Scanagatta (2018) <doi:10.1007/s10994-018-5701-9>, Mauro Scanagatta (2018) <http://proceedings.mlr.press/v73/scanagatta17a.html>; (3) bounded treewidth structure optimization - Mauro Scanagatta (2016) <http://papers.nips.cc/paper/6232-learning-treewidth-bounded-bayesian-networks-with-thousands-of-variables>; (4) structure learning on incomplete data sets - Mauro Scanagatta (2018) <doi:10.1016/j.ijar.2018.02.004>. Distributed under the LGPL-3 by IDSIA.
	"""
	
	cran = "r.blip" 

	version("1.1", md5="2a108f993e391e97db2e4c596692b465")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-bnlearn@4:", type=("build", "run"))
	depends_on("openjdk@1.5:", type=("build", "link", "run"))
