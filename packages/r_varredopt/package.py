# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVarredopt(RPackage):
	"""A Framework for Variance Reduction

	In order to make it easy to use variance reduction algorithms for any simulation, this framework can help you.
    We propose user friendly and easy to extend framework. Antithetic Variates, Inner Control Variates,
    Outer Control Variates and Importance Sampling algorithms are available in the framework. User can
    write its own simulation function and use the Variance Reduction techniques in this package to
    obtain more efficient simulations. An implementation of Asian Option simulation is already 
    available within the package. See Kemal Dinçer Dingeç & Wolfgang Hörmann (2012) <doi:10.1016/j.ejor.2012.03.046>.
	"""
	
	cran = "VarRedOpt" 

	version("0.1.0", md5="9099ed4ca0239a3d81c9d8fd048755a2")

