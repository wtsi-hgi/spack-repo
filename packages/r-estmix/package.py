# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REstmix(RPackage):
	"""Tumor Clones Percentage Estimations

	Includes R functions for the estimation of tumor clones percentages for both snp data and (whole) genome sequencing data. See Cheng, Y., Dai, J. Y., Paulson, T. G., Wang, X., Li, X., Reid, B. J., & Kooperberg, C. (2017). Quantification of multiple tumor clones using gene array and sequencing data. The Annals of Applied Statistics, 11(2), 967-991, <doi:10.1214/17-AOAS1026> for more details.
	"""
	
	cran = "EstMix" 

	version("1.0.1", md5="9cfdc9054540f470be8333d3e51169b2")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-pscbs", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
