# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDipm(RPackage):
	"""Depth Importance in Precision Medicine (DIPM) Method

	An implementation by Chen, Li, and Zhang (2022) <doi: 10.1093/bioadv/vbac041> of the Depth Importance in Precision Medicine (DIPM) method 
             in Chen and Zhang (2022) <doi:10.1093/biostatistics/kxaa021> and Chen and 
             Zhang (2020) <doi:10.1007/978-3-030-46161-4_16>. The DIPM method is a classification 
             tree that searches for subgroups with especially poor or strong performance in a given treatment group.
	"""
	
	cran = "dipm" 

	version("1.9", md5="2e317a3fcf7bb395589ae0b33903a998")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-partykit@1.2.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
