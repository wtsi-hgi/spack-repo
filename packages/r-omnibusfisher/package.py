# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmnibusfisher(RPackage):
	"""A Modified Fisher’s Method to Test Overall Gene-Level Effect

	The separate p-values of SNPs, RNA expressions and DNA
    methylations are calculated by KM regression. The correlation between
    different omics data are taken into account. This method can be applied to
    either samples with all three types of omics data or samples with two types.
	"""
	
	cran = "OmnibusFisher" 

	version("1.0", md5="ac9574e108fd26b8678e17eb92c981d5")

	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
