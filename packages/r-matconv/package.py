# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatconv(RPackage):
	"""A Code Converter from the Matlab/Octave Language to R

	Transferring over a code base from Matlab to R is often a repetitive
    and inefficient use of time. This package provides a translator for Matlab /
    Octave code into R code. It does some syntax changes, but most of the heavy
    lifting is in the function changes since the languages are so similar.
    Options for different data structures and the functions that can be changed
    are given. The Matlab code should be mostly in adherence to the standard
    style guide but some effort has been made to accommodate different number of
    spaces and other small syntax issues. This will not make the code more R
    friendly and may not even run afterwards. However, the rudimentary syntax,
    base function and data structure conversion is done quickly so that the
    maintainer can focus on changes to the design structure.
	"""
	
	cran = "matconv" 

	version("0.4.2", md5="673ecd93a6e69dc11bd9914f255e1818")

