# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDescriptiverepresentationcalculator(RPackage):
	"""Descriptive Representation Calculator: Characterizing Observed
and Expected Representation

	A system for analyzing descriptive representation, especially for comparing the composition of a political body to the population it represents. Users can compute the expected degree of representation for a body under a random sampling model, the expected degree of representation variability, as well as representation scores from observed political bodies. The package is based on Gerring, Jerzak, and Oncel (2023) <doi:10.1017/S0003055423000680>.
	"""
	
	homepage = "https://github.com/cjerzak/DescriptiveRepresentationCalculator-software/"
	cran = "DescriptiveRepresentationCalculator" 

	version("1.0.0", md5="cf17ec0e5e3d5fa7efe06dce49610bf5")

	depends_on("r@3.3.3:", type=("build", "run"))
