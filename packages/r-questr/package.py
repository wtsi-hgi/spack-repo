# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuestr(RPackage):
	"""Constructing Quantitative Environment Sensor using
Transcriptomes

	A method for prediction of environmental conditions based on 
    transcriptome data linked with the environmental gradients. This package 
    provides functions to overview gene-environment relationships, to construct 
    the prediction model, and to predict environmental conditions where the 
    transcriptomes were generated. This package can quest for candidate genes 
    for the model construction even in non-model organisms' transcriptomes 
    without any genetic information. 
	"""
	
	homepage = "https://github.com/takakoizumi/QuESTr"
	cran = "QuESTr" 

	version("0.1.1", md5="056abb050f9725e5c9031c1f35b29be7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
