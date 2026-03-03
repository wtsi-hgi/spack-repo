# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppcgal(RPackage):
	"""'Rcpp' Integration for 'CGAL'

	Creates a header only package to link to the 'CGAL' 
  (Computational Geometry Algorithms Library)
  header files in 'Rcpp'. There are a variety of potential uses for 
  the software such as Hilbert sorting, K-D Tree nearest neighbors, 
  and convex hull algorithms. For more information about how to use the header files, 
  see the 'CGAL' documentation at <https://www.cgal.org>. Currently
  downloads the 'CGAL' version 5.6 stable release.
	"""
	
	homepage = "https://github.com/ericdunipace/RcppCGAL"
	cran = "RcppCGAL" 

	version("5.6.2", md5="76e3077aa7a493c0778ca57ca073cfd8")

	depends_on("r-rcpp", type=("build", "run"))
