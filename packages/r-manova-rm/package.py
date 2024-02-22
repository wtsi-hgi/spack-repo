# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RManovaRm(RPackage):
	"""Resampling-Based Analysis of Multivariate Data and Repeated
Measures Designs

	Implemented are various tests for semi-parametric repeated measures
    and general MANOVA designs that do neither assume multivariate normality nor
    covariance homogeneity, i.e., the procedures are applicable for a wide range
    of general multivariate factorial designs. In addition to asymptotic inference
    methods, novel bootstrap and permutation approaches are implemented as well. These provide more
    accurate results in case of small to moderate sample sizes. Furthermore, post-hoc 
    comparisons are provided for the multivariate analyses.
    Friedrich, S., Konietschke, F. and Pauly, M. (2019) <doi:10.32614/RJ-2019-051>.
	"""
	
	homepage = "https://github.com/smn74/MANOVA.RM"
	cran = "MANOVA.RM" 

	version("0.5.4", md5="5f68f922027963bd710a5ec6c3aaf5fc")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
	depends_on("r-mass@7.3.51:", type=("build", "run"))
	depends_on("r-matrix@1.2.17:", type=("build", "run"))
	depends_on("r-magic@1.5.9:", type=("build", "run"))
	depends_on("r-plotrix@3.5.12:", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-data-table@1.12.6:", type=("build", "run"))
