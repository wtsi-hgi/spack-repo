# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNegenes(RPackage):
	"""Estimating the Number of Essential Genes in a Genome

	Estimating the number of essential genes in a genome on
    the basis of data from a random transposon mutagenesis experiment,
    through the use of a Gibbs sampler.
    Lamichhane et al. (2003) <doi:10.1073/pnas.1231432100>.
	"""
	
	homepage = "https://github.com/kbroman/negenes"
	cran = "negenes" 

	version("1.0-12", md5="33c21ea630e69020be8dfe20b23df4ed")

	depends_on("r@2.10.1:", type=("build", "run"))
