# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCwot(RPackage):
	"""Cauchy Weighted Joint Test for Pharmacogenetics Analysis

	A flexible and robust joint test of the single nucleotide polymorphism (SNP) main effect and genotype-by-treatment interaction effect for continuous and binary endpoints. Two analytic procedures, Cauchy weighted joint test (CWOT) and adaptively weighted joint test (AWOT), are proposed to accurately calculate the joint test p-value. The proposed methods are evaluated through extensive simulations under various scenarios. The results show that the proposed AWOT and CWOT control type I error well and outperform existing methods in detecting the most interesting signal patterns in pharmacogenetics (PGx) association studies. For reference, see Hong Zhang, Devan Mehrotra and Judong Shen (2022) <doi:10.13140/RG.2.2.28323.53280>.
	"""
	
	cran = "cwot" 

	version("0.1.0", md5="e24bfd78d32ba3a8d3f4f1299e096692")

	depends_on("r-spatest", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
