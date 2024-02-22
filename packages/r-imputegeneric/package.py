# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImputegeneric(RPackage):
	"""Ease the Implementation of Imputation Methods

	The general workflow of most imputation methods is quite
    similar. The aim of this package is to provide parts of this general
    workflow to make the implementation of imputation methods easier. The
    heart of an imputation method is normally the used model. These models
    can be defined using the 'parsnip' package or customized
    specifications. The rest of an imputation method are more technical
    specification e.g. which columns and rows should be used for
    imputation and in which order. These technical specifications can be
    set inside the imputation functions.
	"""
	
	homepage = "https://github.com/torockel/imputeGeneric"
	cran = "imputeGeneric" 

	version("0.1.0", md5="30839b2fde1b375dbc304b2b6b9e10de")

	depends_on("r-gower", type=("build", "run"))
	depends_on("r-parsnip", type=("build", "run"))
