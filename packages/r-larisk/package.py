# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLarisk(RPackage):
	"""Estimation of Lifetime Attributable Risk of Cancer from
Radiation Exposure

	Compute lifetime attributable risk of 
    radiation-induced cancer reveals that it can be helpful with 
    enhancement of the flexibility in research with fast calculation 
    and various options. Important reference papers include
    Berrington de Gonzalez et al. (2012) <doi:10.1088/0952-4746/32/3/205>,
    National Research Council (2006, ISBN:978-0-309-09156-5).
	"""
	
	cran = "LARisk" 

	version("1.0.0", md5="738f621644d041b7293be0f3a480203f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
