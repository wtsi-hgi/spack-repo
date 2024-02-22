# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGee(RPackage):
	"""Generalized Estimation Equation Solver

	Generalized Estimation Equation solver.
	"""
	
	cran = "gee" 

	version("4.13-26", md5="0dfe58c9fb7b6f6627d0b501eb3ba15e")

