# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpiinvert(RPackage):
	"""Variational Techniques in Epidemiology

	Using variational techniques we address some epidemiological
  problems as the incidence curve decomposition by inverting the renewal 
  equation as described in Alvarez et al. (2021) <doi:10.1073/pnas.2105112118> 
  and Alvarez et al. (2022) <doi:10.3390/biology11040540> or the estimation of 
  the functional relationship between epidemiological indicators. We also 
  propose a learning method for the short time forecast of the trend 
  incidence curve  as described in 
  Morel et al. (2022) <doi:10.1101/2022.11.05.22281904>.
	"""
	
	homepage = "https://github.com/lalvarezmat/EpiInvert"
	cran = "EpiInvert" 

	version("0.3.1", md5="b7016c3f3cdba926bc44ad08b1d4ece4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
