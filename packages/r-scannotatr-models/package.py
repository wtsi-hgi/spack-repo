# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScannotatrModels(RPackage):
	"""Pretrained models for scAnnotatR package

	Pretrained models for scAnnotatR package. These models can be used to automatically classify several (immune) cell types in human scRNA-seq data.
	"""
	
	bioc = "scAnnotatR.models"

	version("0.99.10", commit="71d030bfbce79487db762cffff13bafb7e22e4d9")
	version("0.99.10", commit="71d030bfbce79487db762cffff13bafb7e22e4d9")

	depends_on("r@4.1:", type=("build", "run"))

