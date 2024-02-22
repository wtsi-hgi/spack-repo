# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHcr(RPackage):
	"""Causal Discovery from Discrete Data using Hidden Compact
Representation

	This code provides a method to fit the hidden compact representation model as well as to identify the causal direction on discrete data. 
    We implement an effective solution to recover the above hidden compact representation under the likelihood framework. 
    Please see the Causal Discovery from Discrete Data using Hidden Compact Representation from NIPS 2018 by Ruichu Cai, Jie Qiao, Kun Zhang, Zhenjie Zhang and Zhifeng Hao (2018) <https://nips.cc/Conferences/2018/Schedule?showEvent=11274> for a description of some of our methods.
	"""
	
	cran = "HCR" 

	version("0.1.1", md5="e226d150bacdc0bb115401def91343de")

	depends_on("r-data-table@1.10.4:", type=("build", "run"))
