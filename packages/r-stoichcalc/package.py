# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStoichcalc(RPackage):
	"""R Functions for Solving Stoichiometric Equations

	Given a list of substance compositions, a list of substances 
  involved in a process, and a list of constraints in addition to mass 
  conservation of elementary constituents, the package contains functions 
  to build the substance composition matrix, to analyze the uniqueness of 
  process stoichiometry, and to calculate stoichiometric coefficients if 
  process stoichiometry is unique. 
  (See Reichert, P. and Schuwirth, N., A generic framework for deriving 
  process stoichiometry in enviromental models, Environmental Modelling 
  and Software 25, 1241-1251, 2010 for more details.)
	"""
	
	cran = "stoichcalc" 

	version("1.1-5", md5="95bdcac54f7efae8804b9107b951ed8e")

