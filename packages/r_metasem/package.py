# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetasem(RPackage):
	"""Meta-Analysis using Structural Equation Modeling

	A collection of functions for conducting meta-analysis using a
             structural equation modeling (SEM) approach via the 'OpenMx' and
             'lavaan' packages. It also implements various procedures to
             perform meta-analytic structural equation modeling on the
             correlation and covariance matrices, see Cheung (2015)
             <doi:10.3389/fpsyg.2014.01521>.
	"""
	
	homepage = "https://github.com/mikewlcheung/metasem"
	cran = "metaSEM" 

	version("1.3.1", md5="337bb1b8d363e86f601cfcce7b896199")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-openmx", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
