# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDotgen(RPackage):
	"""Gene-Set Analysis via Decorrelation by Orthogonal Transformation

	Decorrelates a set of summary statistics (i.e., Z-scores or P-values per SNP) via Decorrelation by Orthogonal Transformation (DOT) approach and performs gene-set analyses by combining transformed statistic values; operations are performed with algorithms that rely only on the association summary results and the linkage disequilibrium (LD). For more details on DOT and its power, see Olga (2020) <doi:10.1371/journal.pcbi.1007819>.
	"""
	
	homepage = "https://github.com/xiaoran831213/dotgen"
	cran = "dotgen" 

	version("0.1.0", md5="cbcd6a9d15dfb50d787bd2f079b403d6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
