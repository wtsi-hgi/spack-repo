# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPklmtest(RPackage):
	"""Classification Based MCAR Test

	Implementation of a KL-based (Kullback-Leibler) test for MCAR (Missing Completely At Random) in the context of missing data as introduced in Michel et al. (2021)  <arXiv:2109.10150>. 
	"""
	
	cran = "PKLMtest" 

	version("1.0.1", md5="bf9b34c8fbb9e2746dce777244aa2d75")

	depends_on("r-ranger", type=("build", "run"))
