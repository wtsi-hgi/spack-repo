# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPowereqtl(RPackage):
	"""Power and Sample Size Calculation for Bulk Tissue and
Single-Cell eQTL Analysis

	Power and sample size calculation for bulk tissue and single-cell eQTL analysis
             based on ANOVA, simple linear regression, or linear mixed effects model. It can also calculate power/sample size 
             for testing the association of a SNP to a continuous type phenotype.
             Please see the reference: Dong X, Li X, Chang T-W, Scherzer CR, Weiss ST, Qiu W. (2021) <doi:10.1093/bioinformatics/btab385>.
	"""
	
	homepage = "https://github.com/sterding/powerEQTL"
	cran = "powerEQTL" 

	version("0.3.4", md5="d85a3894410c08f489af2959821808ea")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-glmmadaptive", type=("build", "run"))
