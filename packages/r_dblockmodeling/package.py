# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDblockmodeling(RPackage):
	"""Deterministic Blockmodeling of Signed, One-Mode and Two-Mode
Networks

	It contains functions to apply blockmodeling of signed (positive and negative weights are assigned to the links), one-mode  and valued one-mode and two-mode (two sets of nodes are considered, e.g. employees and organizations) networks (Brusco et al. (2019) <doi:10.1111/bmsp.12192>).
	"""
	
	cran = "dBlockmodeling" 

	version("0.2.3", md5="9e403ec6b4106d162a5f530ca0647603")

