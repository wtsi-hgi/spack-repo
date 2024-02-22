# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorpora(RPackage):
	"""Statistics and Data Sets for Corpus Frequency Data

	Utility functions for the statistical analysis of corpus frequency data.
        This package is a companion to the open-source course "Statistical Inference: 
        A Gentle Introduction for Computational Linguists and Similar Creatures" ('SIGIL').
	"""
	
	homepage = "http://SIGIL.R-Forge.R-Project.org/"
	cran = "corpora" 

	version("0.6", md5="96face5f62fc886e3036bf8e1d2001b5")

	depends_on("r@3.5:", type=("build", "run"))
