# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNatNblast(RPackage):
	"""NeuroAnatomy Toolbox ('nat') Extension for Assessing Neuron
Similarity and Clustering

	Extends package 'nat' (NeuroAnatomy Toolbox) by providing a
    collection of NBLAST-related functions for neuronal morphology comparison (Costa et al. (2016) <doi: 10.1016/j.neuron.2016.06.012>).
	"""
	
	homepage = "https://natverse.org/nat.nblast/"
	cran = "nat.nblast" 

	version("1.6.7", md5="cd6563ede934f202efea3bb0951b7871")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-nat@1.5.12:", type=("build", "run"))
	depends_on("r-nabor", type=("build", "run"))
	depends_on("r-dendroextras", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-spam", type=("build", "run"))
