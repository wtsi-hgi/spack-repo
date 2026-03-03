# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAhptools(RPackage):
	"""Consistency in the Analytic Hierarchy Process

	A Swiss Army knife of utility functions for users of the Analytic
    Hierarchy Process (AHP) which will help you to assess the consistency of a
    PCM as well as to improve its consistency ratio, to compute the sensitivity
    of a PCM, create a logical, not a random PCM, from the preferences you 
    provide for the alternatives, and a function that helps evaluate the actual
    consistency of a PCM based on objective, fair bench marking. The various
    functions in the toolkit additionally provide the flexibility to users to 
    specify only the upper triangular comparison ratios of the PCM in order to
    performs its assigned task.  
	"""
	
	homepage = "https://CRAN.R-project.org/package=AHPtools"
	cran = "AHPtools" 

	version("0.2.1", md5="49ad1c6e69d448b121e38883d4d19222")

