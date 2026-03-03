# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFasttextr(RPackage):
	"""An Interface to the 'fastText' Library

	An interface to the 'fastText' library
	<https://github.com/facebookresearch/fastText>. The package
	can be used for text classification and to learn word vectors.
	An example how to use 'fastTextR' can be found in the 'README' file.
	"""
	
	homepage = "https://github.com/EmilHvitfeldt/fastTextR"
	cran = "fastTextR" 

	version("2.1.0", md5="7af5db1b3540f6252f37d5d6d945a82f")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
