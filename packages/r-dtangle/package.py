# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDtangle(RPackage):
	"""Cell Type Deconvolution from Gene Expressions

	Deconvolving cell types from high-throughput gene profiling data. For more information on dtangle see Hunt et al. (2019) <doi:10.1093/bioinformatics/bty926>.
	"""
	
	cran = "dtangle" 

	version("2.0.9", md5="c9744317ddbfaa3ed02eb25ca7f65f4a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-deoptimr", type=("build", "run"))
