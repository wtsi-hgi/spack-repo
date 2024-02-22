# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNametagger(RPackage):
	"""Named Entity Recognition in Texts using 'NameTag'

	Wraps the 'nametag' library <https://github.com/ufal/nametag>, allowing users to find and extract entities (names, persons, locations, addresses, ...) in raw text and build your own entity recognition models.
    Based on a maximum entropy Markov model which is described in Strakova J., Straka M. and Hajic J. (2013) <https://ufal.mff.cuni.cz/~straka/papers/2013-tsd_ner.pdf>.
	"""
	
	homepage = "https://github.com/bnosac/nametagger"
	cran = "nametagger" 

	version("0.1.3", md5="3f84acd0225db6b1dcd4427b7900de6f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
