# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmegag(RPackage):
	"""Omega-Generic: Composite Reliability of Multidimensional
Measures

	
    It is a computer tool to estimate the item-sum score's reliability (composite reliability, CR) in multidimensional scales with overlapping items. An item that measures more than one domain construct is called an overlapping item. 
    The estimation is based on factor models allowing unlimited cross-factor loadings such as exploratory structural equation modeling (ESEM) and Bayesian structural equation modeling (BSEM). The factor models include correlated-factor models and bi-factor models. Specifically for bi-factor models, a type of hierarchical factor model, the package estimates the CR hierarchical subscale/hierarchy and CR subscale/scale total. The CR estimator 'Omega-generic' was proposed by Mai, Srivastava, and Krull (2021) <https://whova.com/embedded/subsession/enars_202103/1450751/1452993/>. The current version can only handle continuous data. 
    Yujiao Mai contributes to the algorithms, R programming, and application example. Deo Kumar Srivastava contributes to the algorithms and the application example. Kevin R. Krull contributes to the application example. The package 'OmegaG' was sponsored by American Lebanese Syrian Associated Charities (ALSAC). However, the contents of 'OmegaG' do not necessarily represent the policy of the ALSAC.
	"""
	
	cran = "OmegaG" 

	version("1.0.1", md5="9d28d08f4d098de414c918e6dd46550c")

	depends_on("r@2.50:", type=("build", "run"))
