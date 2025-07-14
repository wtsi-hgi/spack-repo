# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScthi(RPackage):
	"""Indentification of significantly activated ligand-receptor interactions across clusters of cells from single-cell RNA sequencing data

	scTHI is an R package to identify active pairs of ligand-receptors from single cells in order to study,among others, tumor-host interactions. scTHI contains a set of signatures to classify cells from the tumor microenvironment.
	"""
	
	bioc = "scTHI"

	version("1.20.0", commit="3a40e88ce4bf2cacd7e58068dc8ab4595ad4814a")
	version("1.14.0", commit="3402b2b4c905d74ec9b1f002a47d946df01648f2")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
