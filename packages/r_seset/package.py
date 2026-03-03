# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeset(RPackage):
	"""Computing Statistically-Equivalent Path Models

	Tools to compute and analyze the set of statistically-equivalent (Gaussian, linear) path models which generate the input precision or (partial) correlation matrix. 
             This procedure is useful for understanding how statistical network models such as the Gaussian Graphical Model (GGM) perform as causal discovery tools. 
             The statistical-equivalence set of a given GGM expresses the uncertainty we have about the sign, size and direction of directed relationships based on the weights matrix of the GGM alone. 
             The derivation of the equivalence set and its use for understanding GGMs as causal discovery tools is described by Ryan, O., Bringmann, L.F., & Schuurman, N.K. (2022) <doi: 10.31234/osf.io/ryg69>.
	"""
	
	cran = "SEset" 

	version("1.0.1", md5="452eeaa04d39d20b1e530b254777b7a8")

	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
