# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqmade(RPackage):
	"""Network Module-Based Model in the Differential Expression
Analysis for RNA-Seq

	A network module-based generalized linear model for differential expression analysis with the count-based sequence data from RNA-Seq.
	"""
	
	cran = "SeqMADE" 

	version("1.0", md5="14674c3fdf5dcb78da29c49b78206536")

	depends_on("r@2.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
