# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDa(RPackage):
	"""Discriminant Analysis for Evolutionary Inference

	Discriminant Analysis (DA) for evolutionary inference (Qin, X. et al, 2020, <doi:10.22541/au.159256808.83862168>), especially for population genetic structure and community structure inference. This package incorporates the commonly used linear and non-linear, local and global supervised learning approaches (discriminant analysis), including Linear Discriminant Analysis of Kernel Principal Components (LDAKPC), Local (Fisher) Linear Discriminant Analysis (LFDA), Local (Fisher) Discriminant Analysis of Kernel Principal Components (LFDAKPC) and Kernel Local (Fisher) Discriminant Analysis (KLFDA). These discriminant analyses can be used to do ecological and evolutionary inference, including demography inference, species identification, and population/community structure inference.
	"""
	
	homepage = "https://xinghuq.github.io/DA/index.html"
	cran = "DA" 

	version("1.2.0", md5="89933f675c059eb02164dc00dc19ee40")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-adegenet", type=("build", "run"))
	depends_on("r-lfda", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-klar", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-rarpack", type=("build", "run"))
