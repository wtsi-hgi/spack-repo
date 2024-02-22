# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTwosigma(RPackage):
	"""DE Analysis for Single-Cell RNA-Sequencing Data

	Implements the TWO-Component Single Cell Model-Based Association Method (TWO-SIGMA) for gene-level differential expression (DE) analysis and DE-based gene set testing of single-cell RNA-sequencing datasets. See Van Buren et al. (2020) <doi:10.1002/gepi.22361> and Van Buren et al. (2021) <doi:10.1101/2021.01.24.427979>.   
	"""
	
	homepage = "https://github.com/edvanburen/twosigma"
	cran = "twosigma" 

	version("1.0.2", md5="d9350b11d333ffca5cfe6bf5cdd9b1c6")

	depends_on("r-multcomp@1.4.13:", type=("build", "run"))
	depends_on("r-glmmtmb", type=("build", "run"))
	depends_on("r-pscl@1.5.5:", type=("build", "run"))
	depends_on("r-pbapply@1.4:", type=("build", "run"))
	depends_on("r-doparallel@1.0.15:", type=("build", "run"))
