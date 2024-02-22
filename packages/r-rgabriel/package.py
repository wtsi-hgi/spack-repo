# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgabriel(RPackage):
	"""Gabriel Multiple Comparison Test and Plot the Confidence
Interval on Barplot

	Analyze multi-level one-way
        experimental designs where there are unequal sample
        sizes and population variance homogeneity can not be assumed.
        To conduct the Gabriel test <doi:10.2307/2286265>, create two vectors: one for your 
        observations and one for the factor level of each observation. 
        The function, rgabriel, conduct the test and save the output as
        a vector to input into the gabriel.plot function, which produces 
        a confidence interval plot for Multiple Comparison.
	"""
	
	homepage = "https://github.com/yufree/rgabriel"
	cran = "rgabriel" 

	version("0.9", md5="93e793dca7069d883c1563a8da4d6a13")

