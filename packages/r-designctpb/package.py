# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDesignctpb(RPackage):
	"""Design Clinical Trials with Potential Biomarker Effect

	Applying 'CUDA' 'GPUs' via 'Numba' for optimal clinical design. It allows the user to utilize a 'reticulate' 'Python' environment and run intensive Monte Carlo simulation to get the optimal cutoff for the clinical design with potential biomarker effect, which can guide the realistic clinical trials.
	"""
	
	homepage = "https://github.com/ubcxzhang/DesignCTPB"
	cran = "DesignCTPB" 

	version("1.1.3", md5="22b5cd3fccacaf5556a46f1be9728c86")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("openssl@1.0.1:", type=("build", "link", "run"))
	depends_on("cuda", type=("build", "link", "run"))
