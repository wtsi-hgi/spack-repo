# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetarnaseq(RPackage):
	"""Meta-Analysis of RNA-Seq Data

	Implementation of two p-value combination techniques (inverse normal and Fisher methods). A vignette is provided to explain how to perform a meta-analysis from two independent RNA-seq experiments.
	"""
	
	cran = "metaRNASeq" 

	version("1.0.7", md5="d0396c7ad92842be20b6a2087b052437")

	depends_on("r@3.5:", type=("build", "run"))
