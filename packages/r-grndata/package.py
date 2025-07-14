# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrndata(RPackage):
	"""Synthetic Expression Data for Gene Regulatory Network Inference

	Simulated expression data for five large Gene Regulatory Networks from different simulators
	"""
	
	bioc = "grndata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/grndata_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/grndata/grndata_1.34.0.tar.gz"]

	version("1.40.0", tag="RELEASE_3_21")
	version("1.34.0", sha256="d58e54525330ecf71e5c5719eef835a1ef242070576cf2fff5d3d096d295e29d")

	depends_on("r@2.10:", type=("build", "run"))

