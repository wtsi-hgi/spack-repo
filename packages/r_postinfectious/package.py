# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPostinfectious(RPackage):
	"""Estimating the Incubation Period Distribution of Post-Infectious
Syndrome

	Functions to estimate the incubation period distribution of post-infectious syndrome which is defined as the time between the symptom onset of the antecedent infection and that of the post-infectious syndrome.
	"""
	
	cran = "postinfectious" 

	version("0.1.0", md5="c88ce3349f9edd2adb9495298c163283")

