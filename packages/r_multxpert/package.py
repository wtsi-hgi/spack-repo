# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultxpert(RPackage):
	"""Common Multiple Testing Procedures and Gatekeeping Procedures

	Implementation of commonly used p-value-based and
        parametric multiple testing procedures (computation of adjusted
        p-values and simultaneous confidence intervals) and parallel
        gatekeeping procedures based on the methodology presented in
        the book "Multiple Testing Problems in Pharmaceutical
        Statistics" (edited by Alex Dmitrienko, Ajit C. Tamhane and
        Frank Bretz) published by Chapman and Hall/CRC Press 2009.
	"""
	
	homepage = "http://multxpert.com/wiki/MultXpert_package"
	cran = "multxpert" 

	version("0.1.1", md5="af320e164ae9b1196b9c65aad80e8744")

	depends_on("r@2.1:", type=("build", "run"))
	depends_on("r-mvtnorm@0.9:", type=("build", "run"))
