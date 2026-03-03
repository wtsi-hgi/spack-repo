# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCombat(RPackage):
	"""A Combined Association Test for Genes using Summary Statistics

	Genome-wide association studies (GWAS) have been widely used for identifying common variants associated with complex diseases. Due to the small effect sizes of common variants, the power to detect individual risk variants is generally low. Complementary to SNP-level analysis, a variety of gene-based association tests have been proposed. However, the power of existing gene-based tests is often dependent on the underlying genetic models, and it is not known a priori which test is optimal.  Here we proposed COMBined Association Test (COMBAT) to incorporate strengths from multiple existing gene-based tests, including VEGAS, GATES and simpleM. Compared to individual tests, COMBAT shows higher overall performance and robustness across a wide range of genetic models. The algorithm behind this method is described in Wang et al (2017) <doi:10.1534/genetics.117.300257>.
	"""
	
	cran = "COMBAT" 

	version("0.0.4", md5="2759ad990f84d4f74a89600d59ca8856")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r@3.2:", type=("build", "run"))
