# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLbpg(RPackage):
	"""The Length-Biased Power Garima Distribution

	The Length-Biased Power Garima distribution for computes the probability density,
    the cumulative density distribution and the quantile function of the distribution, 
    and generates sample values with random variables based on Kittipong and Sirinapa(2021)<DOI: 10.14456/sjst-psu.2021.89>.
	"""
	
	cran = "LBPG" 

	version("0.1.2", md5="fa21c1687e9278e77c338877ac53e2d5")

	depends_on("r-gsl", type=("build", "run"))
