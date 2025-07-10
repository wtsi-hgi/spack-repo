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
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/scAnnotatR.models_0.99.10.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/scAnnotatR.models/scAnnotatR.models_0.99.10.tar.gz"]

	version("0.99.10", sha256="843e7c6de9132ebd91f2e8ba3fd3ec4caa6362366651b489d6abf4a9bc1c42d6")

	depends_on("r@4.1:", type=("build", "run"))

