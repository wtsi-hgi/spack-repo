# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSegmetric(RPackage):
	"""Metrics for Assessing Segmentation Accuracy for Geospatial Data

	A system that computes metrics to assess the segmentation 
    accuracy of geospatial data. These metrics calculate the discrepancy 
    between segmented and reference objects, and indicate the segmentation 
    accuracy. For more details on choosing evaluation metrics, we 
    suggest seeing Costa et al. (2018) <doi:10.1016/j.rse.2017.11.024> and 
    Jozdani et al. (2020) <doi:10.1016/j.isprsjprs.2020.01.002>.
	"""
	
	homepage = "https://michellepicoli.github.io/segmetric/"
	cran = "segmetric" 

	version("0.3.0", md5="0c38160d9444334860ba5c23b8294aa7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
