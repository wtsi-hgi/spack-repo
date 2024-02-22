# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUngroup(RPackage):
	"""Penalized Composite Link Model for Efficient Estimation of
Smooth Distributions from Coarsely Binned Data

	Versatile method for ungrouping histograms (binned count data) 
 assuming that counts are Poisson distributed and that the underlying sequence 
 on a fine grid to be estimated is smooth. The method is based on the composite 
 link model and estimation is achieved by maximizing a penalized likelihood. 
 Smooth detailed sequences of counts and rates are so estimated from the binned 
 counts. Ungrouping binned data can be desirable for many reasons: Bins can be 
 too coarse to allow for accurate analysis; comparisons can be hindered when 
 different grouping approaches are used in different histograms; and the last 
 interval is often wide and open-ended and, thus, covers a lot of information 
 in the tail area. Age-at-death distributions grouped in age classes and 
 abridged life tables are examples of binned data. Because of modest assumptions, 
 the approach is suitable for many demographic and epidemiological applications. 
 For a detailed description of the method and applications see 
 Rizzi et al. (2015) <doi:10.1093/aje/kwv020>.
	"""
	
	homepage = "https://github.com/mpascariu/ungroup"
	cran = "ungroup" 

	version("1.4.4", md5="20d4fd6f3b98e5965f677442a5f872eb")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-pbapply@1.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack@0.8:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
