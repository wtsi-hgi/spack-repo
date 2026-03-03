# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlaster(RPackage):
	"""Native R Implementation of an Efficient BLAST-Like Algorithm

	Implementation of an efficient BLAST-like sequence
             comparison algorithm, written in 'C++11' and using
             native R datatypes. Blaster is based on 'nsearch' -
             Schmid et al (2018) <doi:10.1101/399782>.
	"""
	
	homepage = "https://github.com/tamminenlab/blaster"
	cran = "blaster" 

	version("1.0.7", md5="80ecfcdc4cbd001e2db5f8a622b96eed")

	depends_on("r-rcpp", type=("build", "run"))
