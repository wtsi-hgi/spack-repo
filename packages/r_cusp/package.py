# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCusp(RPackage):
	"""Cusp-Catastrophe Model Fitting Using Maximum Likelihood

	Cobb's maximum likelihood method for cusp-catastrophe modeling
        (Grasman, van der Maas, and Wagenmakers (2009) <doi:10.18637/jss.v032.i08>;
        Cobb (1981), Behavioral Science, 26(1), 75-78). Includes a cusp() function for model 
        fitting, and several utility functions for plotting, and for comparing the
        model to linear regression and logistic curve models.
	"""
	
	cran = "cusp" 

	version("2.3.6", md5="792f41d37f47fb44fb828605890309ec")

