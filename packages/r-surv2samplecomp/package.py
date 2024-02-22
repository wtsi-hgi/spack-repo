# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurv2samplecomp(RPackage):
	"""Inference for Model-Free Between-Group Parameters for Censored
Survival Data

	Performs inference of several model-free group contrast measures, which include difference/ratio of cumulative incidence rates at given time points, quantiles, and restricted mean survival times (RMST). Two kinds of covariate adjustment procedures (i.e., regression and augmentation) for inference of the metrics based on RMST are also included.
	"""
	
	cran = "surv2sampleComp" 

	version("1.0-5", md5="e154bb8d1db21080d952674c3a23f6e7")

	depends_on("r-flexsurv", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
