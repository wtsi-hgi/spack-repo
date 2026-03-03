# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlegp(RPackage):
	"""Maximum Likelihood Estimates of Gaussian Processes

	Maximum likelihood Gaussian process modeling for
        univariate and multi-dimensional outputs with diagnostic plots 
        following Santner et al (2003) <doi:10.1007/978-1-4757-3799-8>.
        Contact the maintainer for a package version that includes 
        sensitivity analysis.
	"""
	
	cran = "mlegp" 

	version("3.1.9", md5="493ed36146ba964663b73a161a45dce6")

