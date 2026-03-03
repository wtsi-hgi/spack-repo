# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlml2r(RPackage):
	"""Maximum Likelihood Estimation of DNA Methylation and
Hydroxymethylation Proportions

	Maximum likelihood estimates (MLE) of the proportions
    of 5-mC and 5-hmC in the DNA using information from BS-conversion,
    TAB-conversion, and oxBS-conversion methods. One can use information from all three methods 
    or any combination of two of them. Estimates are based on Binomial model by
    Qu et al. (2013) <doi:10.1093/bioinformatics/btt459> and
    Kiihl et al. (2019) <doi:10.1515/sagmb-2018-0031>.
	"""
	
	homepage = "https://github.com/samarafk/MLML2R"
	cran = "MLML2R" 

	version("0.3.3", md5="4aee7829d2963ff272759c980d6cb0bb")

