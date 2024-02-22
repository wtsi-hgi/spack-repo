# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROfgem(RPackage):
	"""A Meta-Analysis Approach with Filtering for Identifying
Gene-Level Gene-Environment Interactions with Genetic
Association Data

	Offers a gene-based meta-analysis test with filtering to detect gene-environment interactions (GxE) with association data, proposed by Wang et al. (2018) <doi:10.1002/gepi.22115>. It first conducts a meta-filtering test to filter out unpromising SNPs by combining all samples in the consortia data. It then runs a test of omnibus-filtering-based GxE meta-analysis (ofGEM) that combines the strengths of the fixed- and random-effects meta-analysis with meta-filtering. It can also analyze data from multiple ethnic groups. 
	"""
	
	homepage = "https://github.com/randel/ofGEM"
	cran = "ofGEM" 

	version("1.0", md5="15c34704f4fa6ac2b8378896db41e1b4")

	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-forestplot", type=("build", "run"))
