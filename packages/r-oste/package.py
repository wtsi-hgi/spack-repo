# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROste(RPackage):
	"""Optimal Survival Trees Ensemble

	Function for growing survival trees ensemble ('Naz Gul', 'Nosheen Faiz', 'Dan Brawn', 'Rafal Kulakowski', 'Zardad Khan', and 'Berthold Lausen' (2020) <arXiv:2005.09043>) is given. 
             The trees are grown by the method of random survival forest ('Marvin Wright', 'Andreas Ziegler' (2017) <doi:10.18637/jss.v077.i01>). 
             The survival trees grown are assessed for both individual and collective performances. 
             The ensemble can give promising results on fewer survival trees selected in the final ensemble.
	"""
	
	cran = "OSTE" 

	version("1.0", md5="c128e9fa76a806fa75fbd37e9e143e38")

	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-pec", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-prodlim", type=("build", "run"))
