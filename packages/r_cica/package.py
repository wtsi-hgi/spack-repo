# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCica(RPackage):
	"""Clusterwise Independent Component Analysis

	Clustering multi-subject resting state functional Magnetic Resonance Imaging data. This methods enables the clustering of subjects based on multi-subject resting state functional Magnetic Resonance Imaging data. Objects are clustered based on similarities and differences in cluster-specific estimated components obtained by Independent Component Analysis.
	"""
	
	homepage = "https://www.sciencedirect.com/science/article/pii/S0165027022002448"
	cran = "CICA" 

	version("1.0.2", md5="2aae9f04a32f56a0c8697276da2ca787")

	depends_on("r-ica", type=("build", "run"))
	depends_on("r-rnifti", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-multiway", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-neurobase", type=("build", "run"))
	depends_on("r-oro-nifti", type=("build", "run"))
	depends_on("r-servr", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
