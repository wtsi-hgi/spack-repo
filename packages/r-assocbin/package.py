# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAssocbin(RPackage):
	"""Measuring Association with Recursive Binning

	An iterative implementation of a recursive binary partitioning algorithm to measure pairwise dependence with a modular design that allows user specification of the splitting logic and stop criteria. Helper functions provide suggested versions of both and support visualization and the computation of summary statistics on final binnings. For a complete description of the functionality and algorithm, see Salahub and Oldford (2023) <arxiv:2311.08561>.
	"""
	
	cran = "AssocBin" 

	version("0.1-0", md5="9b8fa71c8943e15067b67f9a43f67197")

	depends_on("r@4.3:", type=("build", "run"))
