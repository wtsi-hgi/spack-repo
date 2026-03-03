# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSppcomb(RPackage):
	"""Combining Different Spatial Datasets in Cancer Risk Estimation

	We propose a novel two-step procedure to combine epidemiological
    data obtained from diverse sources with the aim to quantify risk factors
    affecting the probability that an individual develops certain disease such as
    cancer. See  Hui Huang, Xiaomei Ma, Rasmus Waagepetersen, Theodore R. Holford,
    Rong Wang, Harvey Risch, Lloyd Mueller & Yongtao Guan (2014) A New Estimation Approach
    for Combining Epidemiological Data From Multiple Sources, Journal of the American Statistical
    Association, 109:505, 11-23,  <doi:10.1080/01621459.2013.870904>.
	"""
	
	cran = "SPPcomb" 

	version("0.1", md5="8c2a6077d408a3a47fd0a70446d44f2c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
