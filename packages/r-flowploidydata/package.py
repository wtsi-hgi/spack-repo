# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowploidydata(RPackage):
	"""Example Flow Cytometry Data

	A collection of raw flow cytometry data for use in vignettes for the flowPloidy package.
	"""
	
	bioc = "flowPloidyData"

	version("1.34.0", commit="bad13407f890d00bd547c3634a6b8008747fa30c")
	version("1.28.0", commit="d4124464a59f1db40abbd3b01ee10adaa66fd304")


