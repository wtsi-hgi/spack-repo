# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPpinfer(RPackage):
	"""Inferring functionally related proteins using protein interaction networks

	Interactions between proteins occur in many, if not most, biological processes. Most proteins perform their functions in networks associated with other proteins and other biomolecules. This fact has motivated the development of a variety of experimental methods for the identification of protein interactions. This variety has in turn ushered in the development of numerous different computational approaches for modeling and predicting protein interactions. Sometimes an experiment is aimed at identifying proteins closely related to some interesting proteins. A network based statistical learning method is used to infer the putative functions of proteins from the known functions of its neighboring proteins on a PPI network. This package identifies such proteins often involved in the same or similar biological functions.
	"""
	
	bioc = "PPInfer"

	version("1.34.0", commit="b01d803a4dc559db9f2dec5b24d5405e4e0a7704")
	version("1.28.0", commit="8fc42656f409f435d0bbb80ccb9c80aecdf33dd8")

	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-fgsea", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-stringdb", type=("build", "run"))
	depends_on("r-yeastexpdata", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
