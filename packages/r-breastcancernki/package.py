# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBreastcancernki(RPackage):
	"""Genexpression dataset published by van't Veer et al. [2002] and van de Vijver et al. [2002] (NKI).

	Genexpression data from a breast cancer study published by van't Veer et al. in 2002 and van de Vijver et al. in 2002, provided as an eSet.
	"""
	
	homepage = "http://compbio.dfci.harvard.edu/"
	bioc = "breastCancerNKI" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/breastCancerNKI_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/breastCancerNKI/breastCancerNKI_1.40.0.tar.gz"]

	version("1.40.0", sha256="3aaac0225fdaa6ad01f064be4efceb4d46d01300bf9a8484b783cb4308de7460")

	depends_on("r@2.5:", type=("build", "run"))

