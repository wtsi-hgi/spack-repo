# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStructfdr(RPackage):
	"""False Discovery Control Procedure Integrating the Prior
Structure Information

	Perform more powerful false discovery control (FDR) for microbiome data, taking into account the prior phylogenetic relationship among bacteria species.  As a general methodology, it is applicable to any type of (genomic) data with prior structure information.
	"""
	
	cran = "StructFDR" 

	version("1.4", md5="f1076c4f7297622a8a32d4d448668c8b")
	version("1.3", md5="1287a00f5361e3362a7ef1afd9f31f51")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-dirmult", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
