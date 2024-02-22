# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlexiblas(RPackage):
	"""'FlexiBLAS' API Interface

	Provides functions to switch the 'BLAS'/'LAPACK' optimized backend
    and change the number of threads without leaving the R session, which needs
    to be linked against the 'FlexiBLAS' wrapper library
    <https://www.mpi-magdeburg.mpg.de/projects/flexiblas>.
	"""
	
	homepage = "https://github.com/Enchufa2/r-flexiblas"
	cran = "flexiblas" 

	version("3.4.0", md5="44e34eafe499e2c8f30cd684aed7cf93")

