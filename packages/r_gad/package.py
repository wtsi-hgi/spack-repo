# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGad(RPackage):
	"""GAD: Analysis of variance from general principles

	This package analyses complex ANOVA models with any
        combination of orthogonal/nested and fixed/random factors, as
        described by Underwood (1997). There are two restrictions: (i)
        data must be balanced; (ii) fixed nested factors are not
        allowed. Homogeneity of variances is checked using Cochran's C
        test and 'a posteriori' comparisons of means are done using
        Student-Newman-Keuls (SNK) procedure.
	"""
	
	cran = "GAD" 

	version("1.1.1", md5="e1af8260e25fcc0f268d6b613ee7f07f")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-r-methodss3", type=("build", "run"))
