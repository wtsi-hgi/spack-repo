# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInsect(RPackage):
	"""Informatic Sequence Classification Trees

	Provides tools for probabilistic taxon assignment with informatic sequence classification trees. See Wilkinson et al (2018) <doi:10.7287/peerj.preprints.26812v1>.
	"""
	
	homepage = "https://github.com/shaunpwilkinson/insect/"
	cran = "insect" 

	version("1.4.2", md5="9a603cb3f6cd7edd1eda93ebeac21cae")

	depends_on("r-ape@3:", type=("build", "run"))
	depends_on("r-aphid@1.3.1:", type=("build", "run"))
	depends_on("r-kmer@1.1:", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-phylogram@2:", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
