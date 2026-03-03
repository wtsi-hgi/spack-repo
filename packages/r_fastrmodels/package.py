# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastrmodels(RPackage):
	"""Models for the 'nflfastR' Package

	A data package that hosts all models for the
    'nflfastR' package.
	"""
	
	homepage = "https://github.com/mrcaseb/fastrmodels"
	cran = "fastrmodels" 

	version("1.0.2", md5="02c6c7f598859feb356146a639d62ec3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-xgboost@1.1:", type=("build", "run"))
