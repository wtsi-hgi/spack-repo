# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLeabra(RPackage):
	"""The Artificial Neural Networks Algorithm Leabra

	The algorithm Leabra (local error driven and associative
    biologically realistic algorithm) allows for the construction of artificial
    neural networks that are biologically realistic and balance supervised and
    unsupervised learning within a single framework. This package is based on
    the 'MATLAB' version by Sergio Verduzco-Flores, which in turn was based on
    the description of the algorithm by Randall O'Reilly (1996)
    <ftp://grey.colorado.edu/pub/oreilly/thesis/oreilly_thesis.all.pdf>. For
    more general (not 'R' specific) information on the algorithm Leabra see
    <https://grey.colorado.edu/emergent/index.php/Leabra>.
	"""
	
	homepage = "https://github.com/johannes-titz/leabRa"
	cran = "leabRa" 

	version("0.1.0", md5="e7a4154e6a588343c557f80b9c3fc81a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
	depends_on("r-r6@2.2.1:", type=("build", "run"))
