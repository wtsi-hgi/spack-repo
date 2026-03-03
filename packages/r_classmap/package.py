# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClassmap(RPackage):
	"""Visualizing Classification Results

	Tools to visualize the results of a classification of cases.
    The graphical displays include stacked plots, silhouette plots, quasi residual plots, and class maps.
    Implements the techniques described and illustrated in Raymaekers, Rousseeuw and Hubert (2021), Class maps for visualizing classification results, Technometrics, appeared online.
    <doi:10.1080/00401706.2021.1927849> (open access) and Raymaekers and Rousseeuw (2021),
    Silhouettes and quasi residual plots for neural nets and tree-based classifiers,
    <arXiv:2106.08814>. Examples can be found in the vignettes:
    "Discriminant_analysis_examples","K_nearest_neighbors_examples",
    "Support_vector_machine_examples", "Rpart_examples", "Random_forest_examples",
    and "Neural_net_examples".
	"""
	
	homepage = "https://doi.org/10.1080/00401706.2021.1927849"
	cran = "classmap" 

	version("1.2.3", md5="558bda90676cc4ab2c3903875feaa0c9")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-cellwise", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
