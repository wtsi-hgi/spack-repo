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

	version("1.40.0", md5="0a0940593d75deaed0aa6f01954cf61c")

	depends_on("r@2.5:", type=("build", "run"))

