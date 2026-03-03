# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTimeseq(RPackage):
	"""Detecting Differentially Expressed Genes in Time Course RNA-Seq
Data

	A negative binomial mixed-effects (NBME) model to detect
    nonparallel differential expression(NPDE) genes and parallel differential
    expression(PDE) genes in the time course RNA-seq data.
	"""
	
	cran = "timeSeq" 

	version("1.0.4", md5="de3bc3d4655876ceefad6d5f93396134")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-gss", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
