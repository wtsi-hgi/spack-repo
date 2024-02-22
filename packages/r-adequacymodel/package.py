# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdequacymodel(RPackage):
	"""Adequacy of Probabilistic Models and General Purpose
Optimization

	The main application concerns to a new robust optimization package with two major contributions. The first contribution refers to the assessment of the adequacy of probabilistic models through a combination of several statistics, which measure the relative quality of statistical models for a given data set. The second one provides a general purpose optimization method based on meta-heuristics functions for maximizing or minimizing an arbitrary objective function.
	"""
	
	homepage = "http://www.r-project.org"
	cran = "AdequacyModel" 

	version("2.0.0", md5="50848456399fc5f60783f80cb4943ebf")

