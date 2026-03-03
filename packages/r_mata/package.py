# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMata(RPackage):
	"""Model-Averaged Tail Area (MATA) Confidence Interval and
Distribution

	Calculates Model-Averaged Tail Area Wald
    (MATA-Wald) confidence intervals, and MATA-Wald confidence densities
    and distributions, which are constructed using single-model
    frequentist estimators and model weights. See Turek and Fletcher
    (2012) <doi:10.1016/j.csda.2012.03.002> and Fletcher et al (2019)
    <doi:10.1007/s10651-019-00432-5> for details.
	"""
	
	cran = "MATA" 

	version("0.7.1", md5="3cebc514ae0072019afe03831088b0e4")

