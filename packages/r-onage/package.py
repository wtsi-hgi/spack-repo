# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnage(RPackage):
	"""Test of Between-Group Differences in the Onset of Senescence

	Implementation of a likelihood ratio test of differential
    onset of senescence between two groups. Given two groups with
    measures of age and of an individual trait likely to be subjected to
    senescence (e.g. body mass), 'OnAge' provides an asymptotic p-value
    for the null hypothesis that senescence starts at the same age in
    both groups. The package implements the procedure used in 
    Douhard et al. (2017) <doi:10.1111/oik.04421>.
	"""
	
	homepage = "https://lbbe.univ-lyon1.fr/OnAge.html"
	cran = "OnAge" 

	version("1.0.1", md5="356166c5a7c00c2304a8b097cd30dd05")

	depends_on("r@3:", type=("build", "run"))
