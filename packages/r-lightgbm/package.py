# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLightgbm(RPackage):
	"""Light Gradient Boosting Machine

	Tree based algorithms can be improved by introducing boosting frameworks.
    'LightGBM' is one such framework, based on Ke, Guolin et al. (2017) <https://papers.nips.cc/paper/6907-lightgbm-a-highly-efficient-gradient-boosting-decision>.
    This package offers an R interface to work with it.
    It is designed to be distributed and efficient with the following advantages:
        1. Faster training speed and higher efficiency.
        2. Lower memory usage.
        3. Better accuracy.
        4. Parallel learning supported.
        5. Capable of handling large-scale data.
    In recognition of these advantages, 'LightGBM' has been widely-used in many winning solutions of machine learning competitions.
    Comparison experiments on public datasets suggest that 'LightGBM' can outperform existing boosting frameworks on both efficiency and accuracy, with significantly lower memory consumption. In addition, parallel experiments suggest that in certain circumstances, 'LightGBM' can achieve a linear speed-up in training time by using multiple machines.
	"""
	
	homepage = "https://github.com/Microsoft/LightGBM"
	cran = "lightgbm" 

	version("4.3.0", md5="8200c6105b4ea2c49e6f83b4c6f0e7dd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-r6@2:", type=("build", "run"))
	depends_on("r-data-table@1.9.6:", type=("build", "run"))
	depends_on("r-jsonlite@1:", type=("build", "run"))
	depends_on("r-matrix@1.1.0:", type=("build", "run"))
