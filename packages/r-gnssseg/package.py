# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGnssseg(RPackage):
	"""Homogenization of GNSS Series

	Homogenize GNSS (Global Navigation Satellite System) time-series. The general model is a segmentation in the mean model including a periodic function and considering monthly variances,  see Quarello (2020) <arXiv:2005.04683>. 
	"""
	
	cran = "GNSSseg" 

	version("6.0", md5="bf344fa1cc46de3506822540f2f76a69")

	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-capushe", type=("build", "run"))
