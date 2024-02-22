# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIndexnumr(RPackage):
	"""Index Number Calculation

	Computes bilateral and multilateral index numbers. 
    It has support for many standard bilateral indexes as well as
    multilateral index number methods such as GEKS, GEKS-Tornqvist 
    (or CCDI), Geary-Khamis and the weighted time product dummy
    (for details on these methods see Diewert and Fox (2020) 
    <doi:10.1080/07350015.2020.1816176>). 
    It also supports updating of multilateral indexes using 
    several splicing methods.
	"""
	
	homepage = "https://github.com/grahamjwhite/IndexNumR"
	cran = "IndexNumR" 

	version("0.6.0", md5="d38f87e8f4d2a35db218e961a0935d8d")

	depends_on("r@3.5:", type=("build", "run"))
