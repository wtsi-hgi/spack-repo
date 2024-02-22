# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcba(RPackage):
	"""CBA Classifier

	Provides implementations of a classifier based on the
    "Classification Based on Associations" (CBA). It can be used for building
    classification models from association rules. Rules are pruned in the order of
    precedence given by the sort criteria and a default rule is added. The final
    classifier labels provided instances. CBA was originally proposed by Liu,
    B. Hsu, W. and Ma, Y. Integrating Classification and Association Rule
    Mining. Proceedings KDD-98, New York, 27-31 August. AAAI. pp80-86 (1998, ISBN:1-57735-070-7).
	"""
	
	homepage = "https://github.com/jaroslav-kuchar/rCBA"
	cran = "rCBA" 

	version("0.4.3", md5="9aedb399dd6b4acc1e452337b8712e0d")

	depends_on("r@3.1.3:", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-arules", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-tunepareto", type=("build", "run"))
	depends_on("openjdk@8:", type=("build", "link", "run"))
