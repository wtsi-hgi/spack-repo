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

	version("1.40.0", commit="19ea80c2c595465d74f5bd31a8974ddf06517e3d")
	version("1.34.0", commit="21a662e1b6fc28dcc9c249b424a8da46dfa37a57")

	depends_on("r@2.10:", type=("build", "run"))

