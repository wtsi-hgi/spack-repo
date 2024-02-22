# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAshapesampler(RPackage):
	"""Generating Alpha Shapes

	Understanding morphological variation is an important task in many applications. Recent studies in computational biology have focused on developing computational tools for the task of sub-image selection which aims at identifying structural features that best describe the variation between classes of shapes. A major part in assessing the utility of these approaches is to demonstrate their performance on both simulated and real datasets. However, when creating a model for shape statistics, real data can be difficult to access and the sample sizes for these data are often small due to them being expensive to collect. Meanwhile, the landscape of current shape simulation methods has been mostly limited to approaches that use black-box inference---making it difficult to systematically assess the power and calibration of sub-image models. In this R package, we introduce the alpha-shape sampler: a probabilistic framework for simulating realistic 2D and 3D shapes based on probability distributions which can be learned from real data or explicitly stated by the user. The 'ashapesampler' package supports two mechanisms for sampling shapes in two and three dimensions. The first, empirically sampling based on an existing data set, was highlighted in the original main text of the paper. The second, probabilistic sampling from a known distribution, is the computational implementation of the theory derived in that paper. Work based on Winn-Nunez et al. (2024) <doi:10.1101/2024.01.09.574919>.
	"""
	
	cran = "ashapesampler" 

	version("1.0.0", md5="1e89b10148da53621acf870ce9ef4ebe")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-alphahull", type=("build", "run"))
	depends_on("r-alphashape3d", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-rvcg", type=("build", "run"))
	depends_on("r-tda", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
