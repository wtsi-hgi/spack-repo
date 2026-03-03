# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMbmixture(RPackage):
	"""Microbiome Mixture Analysis

	Evaluate whether a microbiome sample is a mixture of two
    samples, by fitting a model for the number of read counts as a
    function of single nucleotide polymorphism (SNP) allele and the
    genotypes of two potential source samples.
    Lobo et al. (2021) <doi:10.1093/g3journal/jkab308>.
	"""
	
	homepage = "https://github.com/kbroman/mbmixture"
	cran = "mbmixture" 

	version("0.4", md5="c058ecac6ffdcda38ee4288aa386eddf")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
