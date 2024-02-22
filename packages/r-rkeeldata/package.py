# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRkeeldata(RPackage):
	"""Datasets from 'KEEL' for it Use in 'RKEEL'

	'KEEL' is a popular Java software for a large number of different knowledge data discovery tasks. Furthermore, 'RKEEL' is a package with a R code layer between R and 'KEEL', for using 'KEEL' in R code. This package includes the datasets from 'KEEL' in .dat format for its use in 'RKEEL' package. For more information about 'KEEL', see <http://www.keel.es/>.
	"""
	
	cran = "RKEELdata" 

	version("1.0.5", md5="8819b422e001ac448607c067992b0afc")

