# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNtsdists(RPackage):
	"""Neutrosophic Distributions

	Computes the pdf, cdf, quantile function and generating random numbers for neutrosophic distributions. This family have been developed by different authors in the recent years. See Patro and Smarandache (2016) <doi:10.5281/zenodo.571153> and Rao et al (2023) <doi:10.5281/zenodo.7832786>.
	"""
	
	homepage = "https://github.com/dmazarei/ntsDists"
	cran = "ntsDists" 

	version("2.0.0", md5="2296f65b2163eee4e3e898e54bb3fc24")

	depends_on("r@3.5:", type=("build", "run"))
