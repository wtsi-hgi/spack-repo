# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHindex(RPackage):
	"""Simulating the Development of h-Index Values

	H-index and h-alpha are a bibliometric indicators. This package 
  provides functions to simulate how these indicators may develop over time for
  a given set of researchers and to visualize the simulation data. 
  The implementation is based on the 'STATA' ado h-index and is described in 
  more detail in Bornmann et al. (2019) <arXiv:1905.11052>. 
	"""
	
	cran = "hindex" 

	version("0.2.0", md5="7bd9282b3f8e825cdd96ba414fba3909")

	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
