# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIvabss(RPackage):
	"""Tools for Independent Vector Analysis

	Independent vector analysis (IVA) is a blind source separation (BSS) model where several datasets are jointly unmixed. This package provides several methods for the unmixing together with some performance measures. For details, see Anderson et al. (2011) <doi:10.1109/TSP.2011.2181836> and Lee et al. (2007) <doi:10.1016/j.sigpro.2007.01.010>.
	"""
	
	cran = "ivaBSS" 

	version("1.0.0", md5="5a65099a3c9fac266ee884e867cda420")

	depends_on("r-bssprep", type=("build", "run"))
