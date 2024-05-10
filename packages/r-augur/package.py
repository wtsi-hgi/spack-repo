# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAugur(RPackage):
	"""Augur is an R package to prioritize cell types involved in the response to an experimental perturbation within high-dimensional single-cell data."""
	
	homepage = "https://github.com/neurorestore/Augur"
	git = "https://github.com/neurorestore/Augur.git"

	version("2024-04-05", commit="3f825b946f21f2b2ccd2331aaf1672ce6615b778")
	
	depends_on("r-dplyr@0.8.0:" type=("build", "run"))
	depends_on("r-purrr@0.3.2:" type=("build", "run"))
	depends_on("r-tibble@2.1.3:" type=("build", "run"))
	depends_on("r-magrittr@1.5:" type=("build", "run"))
	depends_on("r-tester@0.1.7:" type=("build", "run"))
	depends_on("r-matrix@1.2-14:" type=("build", "run"))
	depends_on("r-sparsematrixstats@0.1.0:" type=("build", "run"))
	depends_on("r-parsnip@0.0.2:" type=("build", "run"))
	depends_on("r-recipes@0.1.4:" type=("build", "run"))
	depends_on("r-rsample@0.0.4:" type=("build", "run"))
	depends_on("r-yardstick@0.0.3:" type=("build", "run"))
	depends_on("r-pbmcapply@1.5.0:" type=("build", "run"))
	depends_on("r-lmtest@0.9-37:" type=("build", "run"))
	depends_on("r-randomforest@4.6-14:" type=("build", "run"))
	depends_on("r-tidyselect@0.2.5:" type=("build", "run"))
	depends_on("r-rlang@0.4.0:" type=("build", "run"))
	depends_on("r-ggplot2@3.0.0:" type=("build", "run"))
	depends_on("r-ggrepel@0.8.2:" type=("build", "run"))
	depends_on("r-pals@1.6:" type=("build", "run"))
	depends_on("r-scales@1.1.1:" type=("build", "run"))
	depends_on("r-tidyr@1.1.2:" type=("build", "run"))
	depends_on("r-glmnet@3.0-2:" type=("build", "run"))
	depends_on("r-viridis@0.5.1:" type=("build", "run"))
	depends_on("r-rdpack@0.7:" type=("build", "run"))
	depends_on("r-matrixgenerics" type=("build", "run"))
	depends_on("r-seurat" type=("build", "run"))
	depends_on("r-monocle3" type=("build", "run"))
	depends_on("r-singlecellexperiment" type=("build", "run"))