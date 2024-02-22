# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGevaco(RPackage):
	"""Joint Test of Gene and GxE Interactions via Varying Coefficients

	A novel statistical model to detect the joint genetic and dynamic gene-environment (GxE) interaction with continuous traits in genetic association studies. It uses varying-coefficient models to account for different GxE trajectories, regardless whether the relationship is linear or not. The package includes one function, GxEtest(), to test a single genetic variant (e.g., a single nucleotide polymorphism or SNP), and another function, GxEscreen(), to test for a set of genetic variants. The method involves a likelihood ratio test described in Crainiceanu, C. M., and Ruppert, D. (2004) <doi:10.1111/j.1467-9868.2004.00438.x>.
	"""
	
	cran = "GEVACO" 

	version("1.0.1", md5="764f408bb1a73d8dba596c51f9ed5bfa")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-rlrsim", type=("build", "run"))
