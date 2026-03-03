# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatgengwas(RPackage):
	"""Genome Wide Association Studies

	Fast single trait Genome Wide Association Studies (GWAS) following 
    the method described in Kang et al. (2010), <doi:10.1038/ng.548>.        
    One of a series of statistical genetic packages for streamlining the 
    analysis of typical plant breeding experiments developed by Biometris.
	"""
	
	homepage = "https://biometris.github.io/statgenGWAS/index.html"
	cran = "statgenGWAS" 

	version("1.0.9", md5="a973336ef41a0ea3edcb1b55778d5d1a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-sommer@3.7.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
