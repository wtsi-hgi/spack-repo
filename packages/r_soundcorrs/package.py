# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoundcorrs(RPackage):
	"""Semi-Automatic Analysis of Sound Correspondences

	A set of tools that can be used in computer-aided analysis of
    sound correspondences between languages, plus several helper functions.
    Analytic functions range from purely qualitative analysis, through
    statistic methods yielding qualitative results, to an entirely
    quantitative approach.
	"""
	
	cran = "soundcorrs" 

	version("0.4.0", md5="6de02ba2c21cdaf5e97de6bad882e478")

	depends_on("r@3.5:", type=("build", "run"))
