# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHhh4contacts(RPackage):
	"""Age-Structured Spatio-Temporal Models for Infectious Disease
Counts

	Meyer and Held (2017) <doi:10.1093/biostatistics/kxw051> present an
    age-structured spatio-temporal model for infectious disease counts. The
    approach is illustrated in a case study on norovirus gastroenteritis in
    Berlin, 2011-2015, by age group, city district and week, using additional
    contact data from the POLYMOD survey. This package contains the data and
    code to reproduce the results from the paper, see 'demo("hhh4contacts")'.
	"""
	
	cran = "hhh4contacts" 

	version("0.13.3", md5="39e36498341bc3fa11dc200316bede94")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-surveillance@1.14:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
