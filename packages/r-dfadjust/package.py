# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDfadjust(RPackage):
	"""Degrees of Freedom Adjustment for Robust Standard Errors

	Computes small-sample degrees of freedom adjustment for
    heteroskedasticity robust standard errors, and for clustered standard errors
    in linear regression. See Imbens and Kolesár (2016)
    <doi:10.1162/REST_a_00552> for a discussion of these adjustments.
	"""
	
	homepage = "https://github.com/kolesarm/Robust-Small-Sample-Standard-Errors"
	cran = "dfadjust" 

	version("1.0.5", md5="732b0cbb26ca3ded06fd7679a6581051")

	depends_on("r@3.6:", type=("build", "run"))
