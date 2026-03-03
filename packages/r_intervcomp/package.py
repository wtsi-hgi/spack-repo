# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntervcomp(RPackage):
	"""Hypothesis Testing Using the Overlapping Interval Estimates

	Performs hypothesis testing
    using the interval estimates (e.g., confidence intervals). The
    non-overlapping interval estimates indicates the statistical
    significance. References to these procedures can be found at
    Noguchi and Marmolejo-Ramos (2016) <doi:10.1080/00031305.2016.1200487>,
    Bonett and Seier (2003) <doi:10.1198/0003130032323>, and
    Lemm (2006) <doi:10.1300/J082v51n02_05>.
	"""
	
	cran = "intervcomp" 

	version("0.1.2", md5="f7efafae6ea1b531496087b64f61ecb3")

