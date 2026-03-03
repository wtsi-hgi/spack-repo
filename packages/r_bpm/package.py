# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBpm(RPackage):
	"""Bayesian Purity Model to Estimate Tumor Purity

	Bayesian purity model to estimate tumor purity using methylation 
    array data (DNA methylation Infinium 450K array data) without reference samples. 
	"""
	
	cran = "BPM" 

	version("1.0.0", md5="bfc0d4a8c7016e4d3a6e7965c23f287f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
