# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCosnet(RPackage):
	"""Cost Sensitive Network for node label prediction on graphs with highly unbalanced labelings

	Package that implements the COSNet classification algorithm. The algorithm predicts node labels in partially labeled graphs where few positives are available for the class being predicted.
	"""
	
	homepage = "https://github.com/m1frasca/COSNet_GitHub"
	bioc = "COSNet" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/COSNet_1.36.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/COSNet/COSNet_1.36.0.tar.gz"]

	version("1.36.0", md5="6648998ac68e41642f1a7bad77e0bb7f")

