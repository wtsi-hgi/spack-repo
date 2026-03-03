# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcsinr(RPackage):
	"""Parallel Constraint Satisfaction Networks in R

	Parallel Constraint Satisfaction (PCS) models are an increasingly
    common class of models in Psychology, with applications to reading and word
    recognition (McClelland & Rumelhart, 1981), judgment and decision making
    (Glöckner & Betsch, 2008; Glöckner, Hilbig, & Jekel, 2014), and several
    other fields (e.g. Read, Vanman, & Miller, 1997). In each of these fields,
    they provide a quantitative model of psychological phenomena, with precise
    predictions regarding choice probabilities, decision times, and often the degree
    of confidence. This package provides the necessary functions to create and
    simulate basic Parallel Constraint Satisfaction networks within R.
	"""
	
	homepage = "https://github.com/felixhenninger/PCSinR"
	cran = "PCSinR" 

	version("0.1.0", md5="6d01442a419837fba67a1e290853e422")

	depends_on("r@3.3.1:", type=("build", "run"))
