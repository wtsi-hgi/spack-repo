# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAssist(RPackage):
	"""A Suite of R Functions Implementing Spline Smoothing Techniques

	Fit various smoothing spline models. Includes an ssr() function for smoothing 
    spline regression, an nnr() function for nonparametric nonlinear regression, an snr() 
    function for semiparametric nonlinear regression, an slm() function for semiparametric 
    linear mixed-effects models, and an snm() function for semiparametric nonlinear 
    mixed-effects models. See Wang (2011) <doi:10.1201/b10954> for an overview.
	"""
	
	homepage = "https://yuedong.faculty.pstat.ucsb.edu/software.html"
	cran = "assist" 

	version("3.1.9", md5="287be01f8761776c643841b7e38a497f")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
