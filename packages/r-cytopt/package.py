# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCytopt(RPackage):
	"""Optimal Transport for Gating Transfer in Cytometry Data with
Domain Adaptation

	Supervised learning from a source distribution (with known segmentation into cell sub-populations) 
             to fit a target distribution with unknown segmentation. It relies regularized optimal transport to directly 
             estimate the different cell population proportions from a biological sample characterized with flow cytometry 
             measurements. It is based on the regularized Wasserstein metric to compare cytometry measurements from 
             different samples, thus accounting for possible mis-alignment of a given cell population across sample 
             (due to technical variability from the technology of measurements). Supervised learning technique based 
             on the Wasserstein metric that is used to estimate an optimal re-weighting of class proportions in a 
             mixture model Details are presented in Freulon P, Bigot J and Hejblum BP (2021) <arXiv:2006.09003>.
	"""
	
	homepage = "https://sistm.github.io/CytOpT-R/"
	cran = "CytOpT" 

	version("0.9.4", md5="5a20310b8f0d91955d33d595382cacfb")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-metbrewer", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-testthat@3:", type=("build", "run"))
	depends_on("python@3.7:", type=("build", "link", "run"))
