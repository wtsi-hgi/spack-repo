# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImpshrinkage(RPackage):
	"""Improved Shrinkage Estimations for Multiple Linear Regression

	A variety of improved shrinkage estimators in the area of statistical analysis: unrestricted; restricted; preliminary test; improved preliminary test; Stein; and positive-rule Stein. More details can be found in chapter 7 of Saleh, A. K. Md. E. (2006) <ISBN: 978-0-471-56375-4>.
	"""
	
	homepage = "https://github.com/mnrzrad/ImpShrinkage"
	cran = "ImpShrinkage" 

	version("1.0.0", md5="ba7371b60c5812d95603cf9b9b8f75ca")

	depends_on("r@2.10:", type=("build", "run"))
