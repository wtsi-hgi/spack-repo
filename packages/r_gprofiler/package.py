# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGprofiler(RPackage):
	"""Interface to the 'g:Profiler' Toolkit

	This package has been deprecated and will not be updated. 
    New users should use the package 'gprofiler2' (<https://CRAN.R-project.org/package=gprofiler2>)
    for up-to-date data and improved functionality.
    Functional enrichment analysis, gene identifier conversion and
    mapping homologous genes across related organisms via the 'g:Profiler' toolkit
    (<https://biit.cs.ut.ee/gprofiler/>).
	"""
	
	cran = "gProfileR" 

	version("0.7.0", md5="0983580ab51807f1fd6bbb4e258474bc")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
