# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGemini(RPackage):
	"""GEMINI: Variational inference approach to infer genetic interactions from pairwise CRISPR screens

	GEMINI uses log-fold changes to model sample-dependent and independent effects, and uses a variational Bayes approach to infer these effects. The inferred effects are used to score and identify genetic interactions, such as lethality and recovery. More details can be found in Zamanighomi et al. 2019 (in press).
	"""
	
	bioc = "gemini" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/gemini_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/gemini/gemini_1.16.0.tar.gz"]

	version("1.22.0", tag="RELEASE_3_21")
	version("1.16.0", sha256="6d3e62a09ac96eaefdd82a7d9b0136fbcd9f51045b4ef7980ffadab4b69ca8b0")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mixtools", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-pbmcapply", type=("build", "run"))
