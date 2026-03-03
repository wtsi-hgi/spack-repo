# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNgbvs(RPackage):
	"""Bayesian Variable Selection for SNP Data using Normal-Gamma

	Posterior distribution of case-control fine-mapping. Specifically, Bayesian variable selection for single-nucleotide polymorphism (SNP) data using the normal-gamma prior. Alenazi A.A., Cox A., Juarez M,. Lin W-Y. and Walters, K. (2019) Bayesian variable selection using partially observed categorical prior information in fine-mapping association studies, Genetic Epidemiology. <doi:10.1002/gepi.22213>.
	"""
	
	cran = "NGBVS" 

	version("0.3.0", md5="786bd9cc7a50c10b670e6b7783b46407")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
