# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCseqpat(RPackage):
	"""Frequent Contiguous Sequential Pattern Mining of Text

	Mines contiguous sequential patterns in text.
	"""
	
	cran = "CSeqpat" 

	version("0.1.2", md5="bacfa88c598bdc4a152d1b274198e08b")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-nlp", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
