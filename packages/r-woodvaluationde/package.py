# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWoodvaluationde(RPackage):
	"""Wood Valuation Germany

	Monetary valuation of wood in German forests
             (stumpage values), including estimations of harvest quantities, 
             wood revenues, and harvest costs. The functions are sensitive to
             tree species, mean diameter of the harvested trees, stand quality,
             and logging method. The functions include estimations for the
             consequences of disturbances on revenues and costs. The underlying
             assortment tables are taken from Offer and Staupendahl (2018) with
             corresponding functions for salable and skidded volume derived in
             Fuchs et al. (in preparation). Wood revenue and harvest cost
             functions were taken from v. Bodelschwingh (2018). The consequences
             of disturbances refer to Dieter (2001), Moellmann and Moehring
             (2017), and Fuchs et al. (2022a, 2022b). For the full references 
             see documentation of the functions, package README, and Fuchs et
             al. (in preparation). Apart from Dieter (2001) and Moellmann and
             Moehring (2017), all functions and factors are based on data from
             HessenForst, the forest administration of the Federal State of
             Hesse in Germany.
	"""
	
	homepage = "https://github.com/Forest-Economics-Goettingen/woodValuationDE"
	cran = "woodValuationDE" 

	version("1.0.1", md5="074a02d40224dfae4c62fc4f9d9d1131")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
