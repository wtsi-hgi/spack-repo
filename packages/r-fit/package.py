# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFit(RPackage):
	"""Transcriptomic Dynamics Models in Field Conditions

	Provides functionality for constructing
    statistical models of transcriptomic dynamics in field conditions.
    It further offers the function to predict expression of a gene given 
    the attributes of samples and meteorological data. Nagano, A. J., Sato, 
    Y., Mihara, M., Antonio, B. A., Motoyama, R., Itoh, H., Naganuma, Y., and 
    Izawa, T. (2012). <doi:10.1016/j.cell.2012.10.048>. Iwayama, K., Aisaka, Y., 
    Kutsuna, N., and Nagano, A. J. (2017). <doi:10.1093/bioinformatics/btx049>.     
	"""
	
	cran = "FIT" 

	version("0.0.6", md5="d65db7c88a47116b059f18be20cf9cb3")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-gglasso@1.4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.2.1.2:", type=("build", "run"))
