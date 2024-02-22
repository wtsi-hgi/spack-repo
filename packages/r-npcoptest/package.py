# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNpcoptest(RPackage):
	"""Non Parametric Test for Detecting Changes in the Copula

	A non parametric test for change points detection in the dependence between the components of multivariate data, with or without (multiple) changes in the marginal distributions. The full details, justification and examples are published in Rohmer (2016) <doi:10.1016/j.spl.2016.06.026>.
	"""
	
	cran = "npcopTest" 

	version("1.03", md5="9673ac8cd77e7021a9bad865b4fb258b")

