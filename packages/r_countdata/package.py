# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCountdata(RPackage):
	"""The Beta-Binomial Test for Count Data

	The beta-binomial test is used for significance analysis of independent samples by Pham et al. (2010) <doi:10.1093/bioinformatics/btp677>. The inverted beta-binomial test is used for paired sample testing, e.g. pre-treatment and post-treatment data, by Pham and Jimenez (2012) <doi:10.1093/bioinformatics/bts394>. 
	"""
	
	cran = "countdata" 

	version("1.3", md5="d2dda6c3f3d3baf64b39113522222fcf")

	depends_on("r@2.10:", type=("build", "run"))
