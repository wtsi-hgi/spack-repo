# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHydrome(RPackage):
	"""Estimating Water Retention and Infiltration Model Parameters
using Experimental Data

	This version 2 of the HydroMe v.1 package estimates the parameters
  in infiltration and water retention models by curve-fitting methods <doi:10.1016/j.cageo.2008.08.011>. The
  models considered are those commonly used in soil science.  It has new models
  for water retention and characteristic curves.
	"""
	
	homepage = "https://CRAN.r-project.org/package=HydroMe"
	cran = "HydroMe" 

	version("2.0-1", md5="3fa42211e60e2a3e34fa3301e776aeef")

