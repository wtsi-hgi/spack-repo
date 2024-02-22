# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesdlmfmri(RPackage):
	"""Statistical Analysis for Task-Based Fmri Data

	The 'BayesDLMfMRI' package performs statistical analysis for task-based functional magnetic resonance imaging (fMRI) data at both individual and group levels. The analysis to detect brain activation at the individual level is based on modeling the fMRI signal using Matrix-Variate Dynamic Linear Models (MDLM). The analysis for the group stage is based on posterior distributions of the state parameter obtained from the modeling at the individual level. In this way, this package offers several R functions with different algorithms to perform inference on the state parameter to assess brain activation for both individual and group stages. Those functions allow for parallel computation when the analysis is performed for the entire brain as well as analysis at specific voxels when it is required.
             References: Cardona-Jiménez (2021) <doi:10.1016/j.csda.2021.107297>;
             Cardona-Jiménez (2021) <arXiv:2111.01318>.
	"""
	
	homepage = "https://github.com/JohnatanLAB/BayesDLMfMRI/"
	cran = "BayesDLMfMRI" 

	version("0.0.3", md5="7db9e7b16f4f54daa54f65f62f5db736")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-oro-nifti", type=("build", "run"))
	depends_on("r-neurobase", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppdist", type=("build", "run"))
