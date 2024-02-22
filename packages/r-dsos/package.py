# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDsos(RPackage):
	"""Dataset Shift with Outlier Scores

	Test for no adverse shift in two-sample comparison when we
    have a training set, the reference distribution, and a test set. The
    approach is flexible and relies on a robust and powerful test
    statistic, the weighted AUC. Technical details are in Kamulete, V. M.
    (2021) <arXiv:1908.04000>. Modern notions of outlyingness such as
    trust scores and prediction uncertainty can be used as the underlying
    scores for example.
	"""
	
	homepage = "https://github.com/vathymut/dsos"
	cran = "dsos" 

	version("0.1.2", md5="52bdef02c802231021350400f933ac04")

	depends_on("r-data-table@1.14.6:", type=("build", "run"))
	depends_on("r-future-apply@1.10:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-scales@1.2.1:", type=("build", "run"))
	depends_on("r-simctest@2.6:", type=("build", "run"))
