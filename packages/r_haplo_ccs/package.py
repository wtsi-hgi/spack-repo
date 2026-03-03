# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHaploCcs(RPackage):
	"""Estimate Haplotype Relative Risks in Case-Control Data

	Haplotype and covariate relative risks in case-control data are estimated by weighted logistic regression. Diplotype probabilities, which are estimated by EM computation with progressive insertion of loci, are utilized as weights. French et al. (2006) <doi:10.1002/gepi.20161>.
	"""
	
	homepage = "https://github.com/vubiostat/haplo.ccs"
	cran = "haplo.ccs" 

	version("1.3.2", md5="f950e55108ec5e8dfc84fd18ca50736f")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-haplo-stats", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
