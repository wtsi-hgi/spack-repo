# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMildsvm(RPackage):
	"""Multiple-Instance Learning with Support Vector Machines

	Weakly supervised (WS), multiple instance (MI) data lives in
    numerous interesting applications such as drug discovery, object
    detection, and tumor prediction on whole slide images. The 'mildsvm'
    package provides an easy way to learn from this data by training
    Support Vector Machine (SVM)-based classifiers. It also contains
    helpful functions for building and printing multiple instance data
    frames. The core methods from 'mildsvm' come from the following
    references: Kent and Yu (2022) <arXiv:2206.14704>; Xiao, Liu, and Hao
    (2018) <doi:10.1109/TNNLS.2017.2766164>; Muandet et al. (2012)
    <https://proceedings.neurips.cc/paper/2012/file/9bf31c7ff062936a96d3c8bd1f8f2ff3-Paper.pdf>;
    Chu and Keerthi (2007) <doi:10.1162/neco.2007.19.3.792>; and Andrews
    et al. (2003)
    <https://papers.nips.cc/paper/2232-support-vector-machines-for-multiple-instance-learning.pdf>.
    Many functions use the 'Gurobi' optimization back-end to improve the
    optimization problem speed; the 'gurobi' R package and associated
    software can be downloaded from <https://www.gurobi.com> after
    obtaining a license.
	"""
	
	homepage = "https://github.com/skent259/mildsvm"
	cran = "mildsvm" 

	version("0.4.0", md5="9548651384b9680a5d66001b171638df")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
