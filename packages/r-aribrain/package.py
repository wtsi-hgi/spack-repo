# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAribrain(RPackage):
	"""All-Resolution Inference

	It performs All-Resolutions Inference (ARI) on functional Magnetic Resonance Image (fMRI) data. As a main feature, 
 it estimates lower bounds for the proportion of active voxels in a set of clusters as, for example, given by a cluster-wise analysis. 
 The method is described in Rosenblatt, Finos, Weeda, Solari, Goeman (2018) <doi:10.1016/j.neuroimage.2018.07.060>.
	"""
	
	cran = "ARIbrain" 

	version("0.2", md5="0dcd84e9920ee32efdb74ea1dd4ef5f9")

	depends_on("r-hommel", type=("build", "run"))
	depends_on("r-rnifti", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
