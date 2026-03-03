# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTpes(RPackage):
	"""Tumor Purity Estimation using SNVs

	A bioinformatics tool for the estimation of the tumor purity from sequencing data. 
    It uses the set of putative clonal somatic single nucleotide variants within copy number neutral
    segments to call tumor cellularity.
	"""
	
	cran = "TPES" 

	version("1.0.0", md5="1c8021dc7d8eeda5926821a3f455785c")

	depends_on("r@2.10:", type=("build", "run"))
