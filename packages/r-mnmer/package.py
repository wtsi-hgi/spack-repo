# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMnmer(RPackage):
	"""'(m,n)-mer' - A Simple Statistical Feature for Sequence
Classification

	The (m,n)-mer is a statistical feature calculated from conditional frequency distributions obtained from a FASTA file. The resulting table, along with class information, is used to create the classification feature matrix. For more information on this method and its benchmarking results, refer to Andrade et al.'s upcoming publication titled "(m,n)-mer - A Simple Statistical Feature for Sequence Classification".
	"""
	
	cran = "mnmer" 

	version("0.99.1", md5="0f418bf0d0fbaf2804d82d60faec756c")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
