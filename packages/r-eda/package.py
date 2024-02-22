# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REda(RPackage):
	"""Energy Decomposition Analysis

	Energy decomposition analysis for measuring contributions of components
             and factors on energy or carbon emission changes, as described in 
             B.W. Ang (2005) <doi:10.1016/j.enpol.2003.10.010>. Includes Log Mean 
             Devisia Index method and multi-year energy decomposition analysis using 
             five methods. Please refer P. Wu (2019) <doi:10.1016/j.jclepro.2019.02.200> 
             to use the package.
	"""
	
	cran = "EDA" 

	version("1.3", md5="a3a3a74d3f25b899090b41e1a183c53b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
