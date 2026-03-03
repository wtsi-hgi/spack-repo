# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBinarydosage(RPackage):
	"""Creates, Merges, and Reads Binary Dosage Files

	Tools to create binary dosage from either VCF
    or GEN files, merge binary dosage files, and read
    binary dosage files.
	"""
	
	cran = "BinaryDosage" 

	version("1.0.0", md5="39b8aed92581ea70f834edd0b9f1961e")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-prodlim", type=("build", "run"))
