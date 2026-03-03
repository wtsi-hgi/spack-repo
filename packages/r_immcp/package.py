# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImmcp(RPackage):
	"""Poly-Pharmacology Toolkit for Traditional Chinese Medicine
Research

	Toolkit for Poly-pharmacology Research of Traditional Chinese Medicine. Based on the
    biological descriptors and drug-disease interaction networks, it can
    analyze the potential poly-pharmacological mechanisms of Traditional Chinese Medicine and be
    used for drug-repositioning in Traditional Chinese Medicine.
	"""
	
	homepage = "https://github.com/YuanlongHu/immcp"
	cran = "immcp" 

	version("1.0.3", md5="73e1542e65eb2fa41213515a24d8e904")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r@4:", type=("build", "run"))
	depends_on("r-clusterprofiler", type=("build", "run"))
	depends_on("r-dose", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-proxyc", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang@1.0.2:", type=("build", "run"))
	depends_on("r-visnetwork@0.3.1:", type=("build", "run"))
	depends_on("r-arules", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggheatmap", type=("build", "run"))
	depends_on("r-factoextra", type=("build", "run"))
