# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCtrlgene(RPackage):
	"""Assess the Stability of Candidate Housekeeping Genes

	A simple way to assess the stability of candidate housekeeping genes is implemented in this package.
	"""
	
	homepage = "http://www.bioinf.com.cn/"
	cran = "ctrlGene" 

	version("1.0.1", md5="14a661dd69352cbbd2ca5967c75e9500")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
