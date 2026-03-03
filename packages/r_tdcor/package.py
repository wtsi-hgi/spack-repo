# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTdcor(RPackage):
	"""Gene Network Inference from Time-Series Transcriptomic Data

	The Time-Delay Correlation algorithm (TDCor) reconstructs the topology of a gene regulatory network (GRN) from time-series transcriptomic data.  The algorithm is described in details in Lavenus et al., Plant Cell, 2015.  It was initially developed to infer the topology of the GRN controlling lateral root formation in Arabidopsis thaliana.  The time-series transcriptomic dataset which was used in this study is included in the package to illustrate how to use it.
	"""
	
	cran = "TDCor" 

	version("0.1-2", md5="a14a4c141ee255ee3981d9fa85326c2e")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
