# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQtl2(RPackage):
	"""Quantitative Trait Locus Mapping in Experimental Crosses

	Provides a set of tools to perform quantitative
    trait locus (QTL) analysis in experimental crosses. It is a
    reimplementation of the 'R/qtl' package to better handle
    high-dimensional data and complex cross designs.
    Broman et al. (2019) <doi:10.1534/genetics.118.301595>.
	"""
	
	homepage = "https://kbroman.org/qtl2/"
	cran = "qtl2" 

	version("0.34", md5="16eb71c19cfcbece59c2949bfa2175c6", url="https://cran.r-project.org/src/contrib/qtl2_0.34.tar.gz")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-yaml@2.1.13:", type=("build", "run"))
	depends_on("r-jsonlite@0.9.17:", type=("build", "run"))
	depends_on("r-data-table@1.10.4.3:", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
