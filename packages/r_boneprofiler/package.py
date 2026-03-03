# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBoneprofiler(RPackage):
	"""Tools to Study Bone Compactness

	Bone Profiler is a scientific method and a software used to model 
    bone section for paleontological and ecological studies. See Girondot and Laurin 
    (2003) <https://www.researchgate.net/publication/280021178_Bone_profiler_A_tool_to_quantify_model_and_statistically_compare_bone-section_compactness_profiles>
    and Gônet, Laurin and Girondot (2022) <https://palaeo-electronica.org/content/2022/3590-bone-section-compactness-model>.
	"""
	
	cran = "BoneProfileR" 

	version("2.4", md5="60d5f444791b12cb8c2a9a9eb012ed53")

	depends_on("r-imager", type=("build", "run"))
	depends_on("r-helpersmg@5.3.1:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
