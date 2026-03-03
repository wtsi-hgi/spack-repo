# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAws(RPackage):
	"""Adaptive Weights Smoothing

	We provide a collection of R-functions implementing
    adaptive smoothing procedures in 1D, 2D and 3D. This includes the
    Propagation-Separation Approach to adaptive smoothing,
   the Intersecting Confidence Intervals (ICI), variational approaches and a non-local means filter.
   The package is described in detail in Polzehl J, Papafitsoros K, Tabelow K (2020). 
   Patch-Wise Adaptive Weights Smoothing in R. Journal of Statistical Software, 95(6), 1-27. 
   <doi:10.18637/jss.v095.i06>,
    Usage of the package in MR imaging is illustrated in Polzehl and Tabelow (2023),
   Magnetic Resonance Brain Imaging, 2nd Ed. Appendix A, Springer, Use R! Series.
   <doi:10.1007/978-3-031-38949-8>.
	"""
	
	homepage = "https://www.wias-berlin.de/people/polzehl/"
	cran = "aws" 

	version("2.5-5", md5="3868993c01ade46eb9289dbb6193df85")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-awsmethods@1.1.1:", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
