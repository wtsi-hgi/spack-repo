# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLdlinkr(RPackage):
	"""Calculating Linkage Disequilibrium (LD) in Human Population
Groups of Interest

	Provides access to the 'LDlink' API (<https://ldlink.nih.gov/?tab=apiaccess>)
    using the R console.  This programmatic access facilitates researchers who are 
    interested in performing batch queries in 1000 Genomes Project (2015) <doi:10.1038/nature15393> 
    data using 'LDlink'. 'LDlink' is an interactive and powerful suite of web-based tools for querying 
    germline variants in human population groups of interest. For more details, please see 
    Machiela et al. (2015) <doi:10.1093/bioinformatics/btv402>.
	"""
	
	homepage = "https://ldlink.nih.gov"
	cran = "LDlinkR" 

	version("1.3.0", md5="0858d5e982859d0fed5eb81e63b2d77b")

	depends_on("r-httr@1.4:", type=("build", "run"))
