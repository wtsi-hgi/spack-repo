# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIndelmiss(RPackage):
	"""Insertion Deletion Analysis While Accounting for Possible
Missing Data

	Genome-wide gene insertion and deletion rates can be modelled in a maximum 
    likelihood framework with the additional flexibility of modelling potential missing 
    data using the models included within. These models simultaneously estimate insertion 
    and deletion (indel) rates of gene families and proportions of "missing" data for 
    (multiple) taxa of interest. The likelihood framework is utilized for parameter 
    estimation. A phylogenetic tree of the taxa and gene presence/absence patterns 
    (with data ordered by the tips of the tree) are required. See Dang et al.
    (2016) <doi:10.1534/genetics.116.191973> for more details.
	"""
	
	cran = "indelmiss" 

	version("1.0.10", md5="fc96dc7a56c17536a0f68fdfba912481")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ape@3.2:", type=("build", "run"))
	depends_on("r-numderiv@2012.9.1:", type=("build", "run"))
	depends_on("r-phangorn@1.99.13:", type=("build", "run"))
