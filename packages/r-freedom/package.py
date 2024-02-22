# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFreedom(RPackage):
	"""Demonstration of Disease Freedom (DDF)

	Implements the formulae required to calculate freedom
    from disease according to Cameron and Baldock (1998)
    <doi:10.1016/S0167-5877(97)00081-0>. These are the
    methods used at the Swedish national veterinary institute (SVA) to
    evaluate the performance of our nation animal disease
    surveillance programmes.
	"""
	
	homepage = "https://github.com/SVA-SE/freedom"
	cran = "freedom" 

	version("1.0.1", md5="6df2e61fd38e6630fcfe97dbcd8417b9")

	depends_on("r@3.6:", type=("build", "run"))
