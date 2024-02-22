# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixfmri(RPackage):
	"""Mixture fMRI Clustering Analysis

	Utilizing model-based clustering (unsupervised)
        for functional magnetic resonance imaging (fMRI) data.
        The developed methods (Chen and Maitra (2023) <doi:10.1002/hbm.26425>)
        include 2D and 3D clustering analyses
        (for p-values with voxel locations) and
        segmentation analyses (for p-values alone) for fMRI data where p-values
        indicate significant level of activation responding to stimulate
        of interesting. The analyses are mainly identifying active
        voxel/signal associated with normal brain behaviors.
        Analysis pipelines (R scripts) utilizing this package
        (see examples in 'inst/workflow/') is also implemented with high
        performance techniques.
	"""
	
	homepage = "https://github.com/snoweye/MixfMRI"
	cran = "MixfMRI" 

	version("0.1-3", md5="2ca844ae96be2cdb0707e68a5c05aad0")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-fftw", type=("build", "run"))
	depends_on("r-mixsim", type=("build", "run"))
	depends_on("r-emcluster", type=("build", "run"))
