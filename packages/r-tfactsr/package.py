# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTfactsr(RPackage):
	"""Enrichment Approach to Predict Which Transcription Factors are
Regulated

	R implementation of 'TFactS' to predict which are the 
    transcription factors (TFs), regulated in a biological condition based on
    lists of differentially expressed genes (DEGs) obtained from transcriptome
    experiments. This package is based on the 'TFactS' concept by 
    Essaghir et al. (2010) <doi:10.1093/nar/gkq149> and expands
    it. It allows users to perform 'TFactS'-like enrichment approach. The
    package can import and use the original catalogue file from the 'TFactS'
    as well as users' defined catalogues of interest that are not supported 
    by 'TFactS' (e.g., Arabidopsis).
	"""
	
	homepage = "https://afukushima.github.io/TFactSR/"
	cran = "TFactSR" 

	version("0.99.0", md5="0abb67fdc4832325808f78dd7ea41f72")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
