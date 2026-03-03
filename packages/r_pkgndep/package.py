# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPkgndep(RPackage):
	"""Analyze Dependency Heaviness of R Packages

	A new metric named 'dependency heaviness' is proposed that measures the number 
    of additional dependency packages that a parent package brings to its child package 
    and are unique to the dependency packages imported by all other parents.  
    The dependency heaviness analysis is visualized by a customized heatmap. 
    The package is described in <doi:10.1093/bioinformatics/btac449>. 
    We have also performed the dependency heaviness analysis on the CRAN/Bioconductor 
    package ecosystem and the results are implemented as a web-based database 
    which provides comprehensive tools for querying dependencies of individual R packages. 
    The systematic analysis on the CRAN/Bioconductor ecosystem is described in 
    <doi:10.1016/j.jss.2023.111610>. From 'pkgndep' version 2.0.0, the heaviness 
    database includes snapshots of the CRAN/Bioconductor ecosystems for many old R versions.
	"""
	
	homepage = "https://github.com/jokergoo/pkgndep"
	cran = "pkgndep" 

	version("1.99.3", md5="b3294532185249adcc3233f89a5d06a2")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-complexheatmap@2.6:", type=("build", "run"))
	depends_on("r-getoptlong", type=("build", "run"))
	depends_on("r-globaloptions", type=("build", "run"))
	depends_on("r-hash", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-brew", type=("build", "run"))
	depends_on("r-biocversion", type=("build", "run"))
