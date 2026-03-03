# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimuclustfactor(RPackage):
	"""Simultaneous Clustering and Factorial Decomposition of Three-Way
Datasets

	Implements two iterative techniques called T3Clus and 3Fkmeans, aimed at simultaneously clustering objects and a factorial dimensionality reduction of variables and occasions on three-mode datasets developed by Vichi et al. (2007) <doi:10.1007/s00357-007-0006-x>. Also, we provide a convex combination of these two simultaneous procedures called CT3Clus and based on a hyperparameter alpha (alpha in [0,1], with 3FKMeans for alpha=0 and T3Clus for alpha= 1) also developed by Vichi et al. (2007) <doi:10.1007/s00357-007-0006-x>. Furthermore, we implemented the traditional tandem procedures of T3Clus (TWCFTA) and 3FKMeans (TWFCTA) for sequential clustering-factorial decomposition (TWCFTA), and vice-versa (TWFCTA) proposed by P. Arabie and L. Hubert (1996) <doi:10.1007/978-3-642-79999-0_1>.
	"""
	
	cran = "simuclustfactor" 

	version("0.0.3", md5="7c0a12ae055bce5664db9f0f290dcb18")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
