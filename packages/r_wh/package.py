# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWh(RPackage):
	"""Enhanced Implementation of Whittaker-Henderson Smoothing

	An enhanced implementation of Whittaker-Henderson smoothing for the gradation 
    of one-dimensional and two-dimensional actuarial tables used to quantify Life Insurance risks.
    'WH' is based on the methods described in Biessy (2023) <doi:10.48550/arXiv.2306.06932>.
    Among other features, it generalizes the original smoothing algorithm to maximum likelihood estimation, 
    automatically selects the smoothing parameter(s) and extrapolates beyond the range of data.
	"""
	
	homepage = "https://github.com/GuillaumeBiessy/WH"
	cran = "WH" 

	version("1.1.0", md5="292b2874528e678d975bc311ec4d20eb")

	depends_on("r@4.2:", type=("build", "run"))
