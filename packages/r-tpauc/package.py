# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTpauc(RPackage):
	"""Estimation and Inference of Two-Way pAUC, pAUC and pODC

	Tools for estimating and inferring two-way partial area under receiver operating characteristic curves (two-way pAUC), partial area under receiver operating characteristic curves (pAUC), and partial area under ordinal dominance curves (pODC). Methods includes Mann-Whitney statistic and Jackknife, etc. 
	"""
	
	homepage = "http://arxiv.org/abs/1508.00298"
	cran = "tpAUC" 

	version("2.1.1", md5="89f035dc6ebb13e199d62f300805e6f2")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
