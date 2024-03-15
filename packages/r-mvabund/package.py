# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvabund(RPackage):
	"""Statistical Methods for Analysing Multivariate Abundance Data

	A set of tools for displaying, modeling and analysing
        multivariate abundance data in community ecology. See
        'mvabund-package.Rd' for details of overall package organization.
        The package is implemented with the Gnu Scientific Library
        (<http://www.gnu.org/software/gsl/>) and 'Rcpp'
        (<http://dirk.eddelbuettel.com/code/rcpp.html>) 'R' / 'C++' classes.
	"""
	
	cran = "mvabund" 

	version("4.2.1", md5="5ff7cf64b64e2d8ca4df9c3d198d3cf4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-tweedie", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-rcppgsl", type=("build", "run"))
