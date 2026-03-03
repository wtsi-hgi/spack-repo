# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDime(RPackage):
	"""Differential Identification using Mixture Ensemble

	A robust identification of differential binding sites method for analyzing ChIP-seq (Chromatin Immunoprecipitation Sequencing) 
    comparing two samples that considers an ensemble of finite mixture models combined with a local false discovery rate (fdr) 
    allowing for flexible modeling of data. Methods for Differential Identification using Mixture Ensemble (DIME) is described in: 
    Taslim et al., (2011) <doi:10.1093/bioinformatics/btr165>.
	"""
	
	cran = "DIME" 

	version("1.3.0", md5="2e7c06954136030bcb9fe307720b0fc0")

