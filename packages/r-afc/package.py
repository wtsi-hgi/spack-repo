# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAfc(RPackage):
	"""Generalized Discrimination Score

	This is an implementation of the Generalized Discrimination Score
    (also known as Two Alternatives Forced Choice Score, 2AFC) for various 
    representations of forecasts and verifying observations. The Generalized 
    Discrimination Score is a generic forecast verification framework which 
    can be applied to any of the following verification contexts: dichotomous, 
    polychotomous (ordinal and nominal), continuous, probabilistic, and ensemble.
    A comprehensive description of the Generalized Discrimination Score, including 
    all equations used in this package, is provided by Mason and Weigel (2009) 
    <doi:10.1175/MWR-D-10-05069.1>.
	"""
	
	cran = "afc" 

	version("1.4.0", md5="374dc6198cbbd2bd66f0efe4f634324b")

