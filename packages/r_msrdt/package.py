# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsrdt(RPackage):
	"""Multi-State Reliability Demonstration Tests (MSRDT)

	This is a implementation of design methods for multi-state reliability demonstration tests (MSRDT) with failure count data, 
    which is associated with the work from the published paper "Multi-state Reliability Demonstration Tests" by Suiyao Chen et al. (2017) <doi:10.1080/08982112.2017.1314493>.
    It implements two types of MSRDT, multiple periods (MP) and multiple failure modes (MFM). 
    For MP, two different scenarios with criteria on cumulative periods (Cum) or separate periods (Sep) are implemented respectively.
    It also provides the implementation of conventional design method, namely binomial tests for failure count data.
	"""
	
	homepage = "https://github.com/ericchen12377/MSRDT"
	cran = "MSRDT" 

	version("0.1.0", md5="4606c8cf803ef396d6f0e2a2e497f4c6")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
