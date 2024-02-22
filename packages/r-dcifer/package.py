# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDcifer(RPackage):
	"""Genetic Relatedness Between Polyclonal Infections

	An implementation of Dcifer (Distance for complex infections: fast estimation of relatedness), an identity by descent (IBD) based method to calculate genetic relatedness between polyclonal infections from biallelic and multiallelic data. The package includes functions that format and preprocess the data, implement the method, and visualize the results. 
    Gerlovina et al. (2022) <doi:10.1093/genetics/iyac126>. 
	"""
	
	homepage = "https://github.com/EPPIcenter/dcifer"
	cran = "dcifer" 

	version("1.2.1", md5="1d1ed47d96dc63c04d550e1d2a4896e6")

	depends_on("r@3.5:", type=("build", "run"))
