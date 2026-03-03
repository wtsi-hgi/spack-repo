# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVfp(RPackage):
	"""Variance Function Program

	
  Variance function estimation for models proposed by W. Sadler in his variance function program 
  ('VFP', <http://www.aacb.asn.au/resources/useful-tools/variance-function-program-v14>). Here, the idea is
  to fit multiple variance functions to a data set and consequently assess which function reflects
  the relationship 'Var ~ Mean' best. For 'in-vitro diagnostic' ('IVD') assays modeling this relationship
  is of great importance when individual test-results are used for defining follow-up treatment of patients.  
	"""
	
	cran = "VFP" 

	version("1.4.1", md5="e264553902a9398dcf84bba558e32ebd")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-gnm", type=("build", "run"))
	depends_on("r-vca", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
