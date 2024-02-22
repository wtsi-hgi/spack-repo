# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSubgxe(RPackage):
	"""Combine Multiple GWAS by Using Gene-Environment Interactions

	Classical methods for combining summary data from genome-wide
    association studies (GWAS) only use marginal genetic effects and power can
    be compromised in the presence of heterogeneity. 'subgxe' is a R package
    that implements p-value assisted subset testing for association (pASTA),
    a method developed by Yu et al. (2019) <doi:10.1159/000496867>. pASTA
    generalizes association analysis based on subsets by incorporating
    gene-environment interactions into the testing procedure.
	"""
	
	homepage = "https://github.com/umich-cphds/subgxe"
	cran = "subgxe" 

	version("0.9.0", md5="23a2efabe04f35bf6ec2d0f1582b9d7e")

