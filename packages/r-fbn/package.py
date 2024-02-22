# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFbn(RPackage):
	"""FISH Based Normalization and Copy Number Inference of SNP
Microarray Data

	Normalizes the data from a file containing the raw values of the SNP probes of microarray data by using the FISH probes and their corresponding copy number.
	"""
	
	cran = "FBN" 

	version("1.5.2", md5="896ebb54b541f3366d55618b4d10754f")

	depends_on("r@2.10:", type=("build", "run"))
