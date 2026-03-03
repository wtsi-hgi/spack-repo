# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSansa(RPackage):
	"""Synthetic Data Generation for Imbalanced Learning in 'R'

	Machine learning is widely used in information-systems design. Yet, training algorithms on imbalanced datasets may severely affect performance on unseen data. For example, in some cases in healthcare, financial, or internet-security contexts, certain sub-classes are difficult to learn because they are underrepresented in training data. This 'R' package offers a flexible and efficient solution based on a new synthetic average neighborhood sampling algorithm ('SANSA'), which, in contrast to other solutions, introduces a novel “placement” parameter that can be tuned to adapt to each datasets unique manifestation of the imbalance. More information about the algorithm's parameters can be found at Nasir et al. (2022) <https://murtaza.cc/SANSA/>. 
	"""
	
	cran = "sansa" 

	version("0.0.1", md5="c9ee185e21a3a2f75fce24cd32b828cf")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
