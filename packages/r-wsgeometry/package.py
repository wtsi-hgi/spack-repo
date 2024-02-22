# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWsgeometry(RPackage):
	"""Geometric Tools Based on Balanced/Unbalanced Optimal Transport

	Includes a variety of methods to compute objects related to the 'Wasserstein distance' (also known as 'Kantorovich distance' or 'Earth-Mover distance'). The main effort of this package is to allow for computations of 'Wasserstein barycenter' using regularised, unregularised and stochastic methods. It also provides convenient wrappers to call the 'transport' package with more general inputs. Handy visual tools are provided to showcase, barycenters, animations of optimal transport geodesics and animations of principal components in the 'Wasserstein space'. It also includes tools to compute 'Kantorovich-Rubinstein' distances and barycenters. 
	"""
	
	cran = "WSGeometry" 

	version("1.2.1", md5="616c5378d411b08fc8e1a422ecdcc878")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-transport", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-imager", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
