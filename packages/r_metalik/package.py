# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetalik(RPackage):
	"""Likelihood Inference in Meta-Analysis and Meta-Regression Models

	First- and higher-order likelihood inference in
        meta-analysis and meta-regression models.
	"""
	
	cran = "metaLik" 

	version("0.43.0", md5="18e52331321ff4444ee91c848fd71dc7")

	depends_on("r@3.4:", type=("build", "run"))
