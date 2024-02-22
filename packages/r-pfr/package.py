# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPfr(RPackage):
	"""Interface to the 'C++' Library 'Pf'

	Builds and runs 'c++' code for classes that encapsulate state space model, particle filtering algorithm pairs.
    Algorithms include the Bootstrap Filter from Gordon et al. (1993) <doi:10.1049/ip-f-2.1993.0015>, the generic SISR filter, 
    the Auxiliary Particle Filter from Pitt et al (1999) <doi:10.2307/2670179>, and a variety of Rao-Blackwellized 
    particle filters inspired by Andrieu et al. (2002) <doi:10.1111/1467-9868.00363>. For more details on the 'c++' library 
    'pf', see Brown (2020) <doi:10.21105/joss.02599>.
	"""
	
	cran = "pfr" 

	version("1.0.1", md5="5b08cb399214c13cce885bc3aa30c1be")

	depends_on("r-inline@0.3.19:", type=("build", "run"))
	depends_on("r-rstudioapi@0.13:", type=("build", "run"))
