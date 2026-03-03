# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMapitr(RPackage):
	"""MArginal ePIstasis Test for Regions

	A genetic analysis tool and variance component 
    model for identifying marginal epistasis between pathways 
    and the rest of the genome. 'MAPITR' uses as input a matrix 
    of genotypes, a vector of phenotypes, and a list of 
    pathways. 'MAPITR' then iteratively tests each pathway for 
    epistasis between any variants within the pathway versus 
    any variants remaining in the rest of the genome. 'MAPITR'
    returns results in the form of p-values for every pathway 
    indicating whether the null model of there being no 
    epistatic interactions between a pathway and the rest of 
    the genome can be rejected.
	"""
	
	homepage = "https://github.com/mturchin20/MAPITR"
	cran = "MAPITR" 

	version("1.1.2", md5="af7dd15031ca9125f5bac382f088a945")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
