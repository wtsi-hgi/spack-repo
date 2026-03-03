# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRocaggregator(RPackage):
	"""Aggregate Multiple ROC Curves into One Global ROC

	Aggregates multiple Receiver Operating Characteristic (ROC) curves 
    obtained from different sources into one global ROC. Additionally, it’s 
    also possible to calculate the aggregated precision-recall (PR) curve.
	"""
	
	homepage = "https://gitlab.com/UM-CDS/general-tools/rocaggregator"
	cran = "ROCaggregator" 

	version("1.0.1", md5="ea4b33d30886ee6a304afb19f2251eba")

	depends_on("r-magrittr", type=("build", "run"))
