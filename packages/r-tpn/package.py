# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTpn(RPackage):
	"""Truncated Positive Normal Model and Extensions

	Provide data generation and estimation tools for the truncated positive normal (tpn)
             model discussed in Gomez, Olmos, Varela and Bolfarine (2018) 
             <doi:10.1007/s11766-018-3354-x>, the slash tpn distribution discussed in Gomez, 
             Gallardo and Santoro (2021) <doi:10.3390/sym13112164>, the bimodal tpn distribution 
             discussed in Gomez et al. (2022) <doi:10.3390/sym14040665> and the flexible tpn model. 
	"""
	
	cran = "tpn" 

	version("1.8", md5="08215827d487ba50b404068d21559c1d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-skewmlrm", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-rbe3", type=("build", "run"))
