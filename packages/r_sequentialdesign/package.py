# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSequentialdesign(RPackage):
	"""Observational Database Study Planning using Exact Sequential
Analysis for Poisson and Binomial Data

	Functions to be used in conjunction with the 'Sequential' package that allows for planning of observational database studies that will be analyzed with exact sequential analysis. This package supports Poisson- and binomial-based data. The primary function, seq_wrapper(...), accepts parameters for simulation of a simple exposure pattern and for the 'Sequential' package setup and analysis functions. The exposure matrix is used to simulate the true and false positive and negative populations (Green (1983) <doi:10.1093/oxfordjournals.aje.a113521>, Brenner (1993) <doi:10.1093/oxfordjournals.aje.a116805>). Functions are then run from the 'Sequential' package on these populations, which allows for the exploration of outcome misclassification in data.
	"""
	
	cran = "SequentialDesign" 

	version("1.0", md5="b4d892f20472e2d54e831331379095f2")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-sequential", type=("build", "run"))
