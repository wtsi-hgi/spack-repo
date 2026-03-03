# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDendrometry(RPackage):
	"""Forest Estimations and Dendrometric Computations

	Computation of dendrometric and structural 
   parameters from forest inventory data. The objective is to provide an 
   user-friendly R package for researchers, ecologists, foresters, 
   statisticians, loggers and others persons who deal with forest inventory 
   data. Useful conversion of angle value from degree to radian, conversion from 
   angle to slope (in percentage) and their reciprocals as well as principal 
   angle determination are also included. Position and dispersion parameters 
   usually found in forest studies are implemented. The package contains 
   Fibonacci series, its extensions and the Golden Number computation.
   Useful references are Arcadius Y. J. Akossou, Soufianou Arzouma, 
   Eloi Y. Attakpa, Noël H. Fonton and Kouami Kokou (2013) <doi:10.3390/d5010099> 
   and W. Bonou, R. Glele Kakaï, A.E. Assogbadjo, H.N. Fonton, B. Sinsin (2009) 
   <doi:10.1016/j.foreco.2009.05.032> .
	"""
	
	cran = "dendrometry" 

	version("0.0.2", md5="1eae5bc6de6622f9ab078ad5b621db6e")

	depends_on("r@3.5:", type=("build", "run"))
