# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDisprofas(RPackage):
	"""Non-Parametric Dissolution Profile Analysis

	Similarity of dissolution profiles is assessed using the
    similarity factor f2 according to the EMA guideline (European
    Medicines Agency 2010) "On the investigation of bioequivalence".
    Dissolution profiles are regarded as similar if the f2 value is
    between 50 and 100. For the applicability of the similarity factor f2,
    the variability between profiles needs to be within certain limits.
    Often, this constraint is violated. One possibility in this situation
    is to resample the measured profiles in order to obtain a bootstrap
    estimate of f2 (Shah et al. (1998) <doi:10.1023/A:1011976615750>).
    Other alternatives are the model-independent non-parametric
    multivariate confidence region (MCR) procedure (Tsong et al. (1996)
    <doi:10.1177/009286159603000427>) or the T2-test for equivalence
    procedure (Hoffelder (2016)
    <https://www.ecv.de/suse_item.php?suseId=Z|pi|8430>). Functions for
    estimation of f1, f2, bootstrap f2, MCR / T2-test for equivalence
    procedure are implemented.
	"""
	
	homepage = "https://github.com/piusdahinden/disprofas"
	cran = "disprofas" 

	version("0.1.3", md5="641387bfa08cb5f71a40f5959f88a385")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
