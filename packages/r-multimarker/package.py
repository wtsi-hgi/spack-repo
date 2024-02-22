# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultimarker(RPackage):
	"""Latent Variable Model to Infer Food Intake from Multiple
Biomarkers

	A latent variable model based on factor analytic and mixture of experts models, designed to infer food intake from multiple biomarkers data. The model is framed within a Bayesian hierarchical framework, which provides flexibility to adapt to different biomarker distributions and facilitates inference on food intake from biomarker data alone, along with the associated uncertainty. Details are in D'Angelo, et al. (2020) <arXiv:2006.02995>.
	"""
	
	cran = "multiMarker" 

	version("1.0.1", md5="0161e19f664103d0f273aceb5f3d10db")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-ordinalnet", type=("build", "run"))
