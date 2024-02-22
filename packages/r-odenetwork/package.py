# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROdenetwork(RPackage):
	"""Network of Differential Equations

	Simulates a network of ordinary differential equations of order
    two. The package provides an easy interface to construct networks. In addition
    you are able to define different external triggers to manipulate the trajectory.
    The method is described by Surmann, Ligges, and Weihs (2014) <doi:10.1109/ENERGYCON.2014.6850482>.
	"""
	
	homepage = "https://github.com/surmann/ODEnetwork"
	cran = "ODEnetwork" 

	version("1.3.2", md5="f631bc8f08260c9e16c84ee1168ff600")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-checkmate@1.5:", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
