# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCascadedata(RPackage):
	"""Experimental Data of Cascade Experiments in Genomics

	These experimental expression data (5 leukemic 'CLL' B-lymphocyte of aggressive form from 'GSE39411', <doi:10.1073/pnas.1211130110>), after B-cell receptor stimulation, are used as examples by packages such as the 'Cascade' one, a modeling tool allowing gene selection, reverse engineering, and prediction in cascade networks. Jung, N., Bertrand, F., Bahram, S., Vallat, L., and Maumy-Bertrand, M. (2014) <doi:10.1093/bioinformatics/btt705>.
	"""
	
	homepage = "https://fbertran.github.io/CascadeData/"
	cran = "CascadeData" 

	version("1.4", md5="d35a74b9b65ca6ce2dbeeb7253406d83")

	depends_on("r@2.10:", type=("build", "run"))
