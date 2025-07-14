# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMulticlust(RPackage):
	"""multiClust: An R-package for Identifying Biologically Relevant Clusters in Cancer Transcriptome Profiles

	Clustering is carried out to identify patterns in transcriptomics profiles to determine clinically relevant subgroups of patients. Feature (gene) selection is a critical and an integral part of the process. Currently, there are many feature selection and clustering methods to identify the relevant genes and perform clustering of samples. However, choosing an appropriate methodology is difficult. In addition, extensive feature selection methods have not been supported by the available packages. Hence, we developed an integrative R-package called multiClust that allows researchers to experiment with the choice of combination of methods for gene selection and clustering with ease. Using multiClust, we identified the best performing clustering methodology in the context of clinical outcome. Our observations demonstrate that simple methods such as variance-based ranking perform well on the majority of data sets, provided that the appropriate number of genes is selected. However, different gene ranking and selection methods remain relevant as no methodology works for all studies.
	"""
	
	bioc = "multiClust"

	version("1.38.0", commit="765fddeab133c9f7dbb2c82e3d3db86df6db7dd4")
	version("1.32.0", commit="62994deba28721f4efc24950dbdfd573f874a2fb")

	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-ctc", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-amap", type=("build", "run"))
