# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmodely(RPackage):
	"""Modeling Multivariate Origins Determinants - Evolutionary
Lineages in Ecology

	
 Perform multivariate modeling of evolved traits, with special attention to
 understanding the interplay of the multi-factorial determinants of their origins
 in complex ecological settings (Stephens, 2007 <doi:10.1016/j.tree.2006.12.003>).
 This software primarily concentrates on phylogenetic regression analysis, enabling
 implementation of tree transformation averaging and visualization functionality.
 Functions additionally support information theoretic approaches
 (Grueber, 2011 <doi:10.1111/j.1420-9101.2010.02210.x>;
 Garamszegi, 2011 <doi:10.1007/s00265-010-1028-7>)
 such as  model averaging and selection of phylogenetic models.
 Accessory functions are also implemented for coef standardization (Cade 2015), 
 selection uncertainty, and variable importance (Burnham & Anderson 2000).
 There are other numerous functions for visualizing confounded variables,
 plotting phylogenetic trees, as well as reporting and exporting modeling results.
 Lastly, as challenges to ecology are inherently multifarious, and therefore often
 multi-dataset, this package features several functions to support the identification,
 interpolation, merging, and updating of missing data and outdated nomenclature.
	"""
	
	cran = "mmodely" 

	version("0.2.5", md5="00b32e0f06c6f8f44d143dcdf32ea760")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-caper", type=("build", "run"))
	depends_on("r-caroline", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
