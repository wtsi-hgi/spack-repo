# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaigegds(RPackage):
	"""Scalable Implementation of Generalized mixed models using GDS files in Phenome-Wide Association Studies

	Scalable implementation of generalized mixed models with highly optimized C++ implementation and integration with Genomic Data Structure (GDS) files. It is designed for single variant tests and set-based aggregate tests in large-scale Phenome-wide Association Studies (PheWAS) with millions of variants and samples, controlling for sample structure and case-control imbalance. The implementation is based on the SAIGE R package (v0.45, Zhou et al. 2018 and Zhou et al. 2020), and it is extended to include the state-of-the-art ACAT-O set-based tests. Benchmarks show that SAIGEgds is significantly faster than the SAIGE R package.
	"""
	
	homepage = "https://github.com/AbbVie-ComputationalGenomics/SAIGEgds"
	bioc = "SAIGEgds"

	version("2.8.0", commit="27c4ea46904ab7ddf55d01acd9a91fafc76508f5")
	version("2.2.1", commit="511d2b86a95f5d0ca0c5e2c05b997136a379f887")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gdsfmt@1.28:", type=("build", "run"))
	depends_on("r-seqarray@1.36.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcppparallel@5:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
