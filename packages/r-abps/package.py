# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbps(RPackage):
	"""The Abnormal Blood Profile Score to Detect Blood Doping

	An implementation of the Abnormal Blood Profile Score (ABPS,
    part of the Athlete Biological Passport program of the World Anti-Doping
    Agency), which combines several blood parameters into a single score in
    order to detect blood doping (Sottas et al. (2006)
    <doi:10.2202/1557-4679.1011>). The package also contains functions to
    calculate other scores used in anti-doping programs, such as the
    OFF-score (Gore et al. (2003) <http://www.haematologica.org/content/88/3/333>),
    as well as example data.
	"""
	
	cran = "ABPS" 

	version("0.3", md5="2f09a946652530e319d433d7f0362be8")

	depends_on("r-kernlab", type=("build", "run"))
