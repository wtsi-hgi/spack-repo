# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutoplotprotein(RPackage):
	"""Development of Visualization Tools for Protein Sequence

	The image of the amino acid transform on the protein level is drawn, and the automatic routing of the functional elements such as the domain and the mutation site is completed.
	"""
	
	cran = "Autoplotprotein" 

	version("1.1", md5="5f125c582838131394798d07c549220d")

	depends_on("r-xml", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
