# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgpicrust2(RPackage):
	"""Make 'PICRUSt2' Output Analysis and Visualization Easier

	Provides a convenient way to analyze and visualize 'PICRUSt2' output with pre-defined plots and functions. Allows for generating statistical plots about microbiome functional predictions and offers customization options. Features a one-click option for creating publication-level plots, saving time and effort in producing professional-grade figures. Streamlines the 'PICRUSt2' analysis and visualization process. For more details, see Yang et al. (2023) <doi:10.1093/bioinformatics/btad470>.
	"""
	
	homepage = "https://github.com/cafferychen777/ggpicrust2"
	cran = "ggpicrust2" 

	version("1.7.3", md5="3739e79972eed6c30f4efc0f2ef16eb0", url="https://cran.r-project.org/src/contrib/ggpicrust2_1.7.3.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-aldex2", type=("build", "run"))
	depends_on("r-aplot", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggh4x", type=("build", "run"))
	depends_on("r-lefser", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-maaslin2", type=("build", "run"))
	depends_on("r-metagenomeseq", type=("build", "run"))
	depends_on("r-microbiomestat", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggprism", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
