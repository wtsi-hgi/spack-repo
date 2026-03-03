# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaascnv(RPackage):
	"""Somatic Copy Number Alteration Analysis Using Sequencing and SNP
Array Data

	Perform joint segmentation on two signal dimensions derived from 
    total read depth (intensity) and allele specific read depth (intensity) for 
    whole genome sequencing (WGS), whole exome sequencing (WES) and SNP array data.
	"""
	
	homepage = "https://zhangz05.u.hpc.mssm.edu/saasCNV/"
	cran = "saasCNV" 

	version("0.3.4", md5="c720ee05bf4ca0ef49adb66bc9a5563d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-dnacopy", type=("build", "run"))
